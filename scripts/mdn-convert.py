#!/usr/bin/env python3
"""MDN WebDriver Documentation Compiler and Sanitizer.

Processes raw MDN Markdown source files directly from the local git repository,
expands KumaScript macros into native Markdown, resolves dynamic child page indexes
(ListSubPages, SubpagesWithSummaries), fetches and injects BCD (Browser Compatibility
Data) tables with parameter rows and contextual notes, sanitizes YAML front-matter,
flattens index.md folder structures into topic-named .md files, and normalizes internal/external links.

Generates a dual-directory output bundle:
- release_bundle/raw_mdn_webdriver/ (Unmodified original MDN source files)
- release_bundle/compiled_mdn_webdriver/ (Processed, flattened, and optimized files)
"""

import json
import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import frontmatter

# Allowed YAML front-matter keys for LLM context optimization
ALLOWED_FRONTMATTER_KEYS = {"title", "slug", "status"}

SOURCE_DIR = Path("mdn-source/files/en-us/web/webdriver")
BUNDLE_DIR = Path("release_bundle")
RAW_OUTPUT_DIR = BUNDLE_DIR / "raw_mdn_webdriver"
COMPILED_OUTPUT_DIR = BUNDLE_DIR / "compiled_mdn_webdriver"

# Inheritance map for browser engines using "mirror" support in BCD
MIRROR_MAP = {
    "edge": "chrome",
    "chrome_android": "chrome",
    "firefox_android": "firefox",
    "safari_ios": "safari",
    "opera": "chrome",
}

# Cache for BCD JSON responses to avoid redundant HTTP requests
BCD_CACHE = {}


def compute_slug(file_path: Path, raw_content: str) -> str:
    """Extracts the slug from YAML front-matter or computes a fallback from file path."""
    slug_match = re.search(r"^slug:\s*(.*)$", raw_content, re.MULTILINE)
    if slug_match and slug_match.group(1).strip():
        return slug_match.group(1).strip()

    rel_path = file_path.relative_to(Path("mdn-source/files/en-us"))
    if rel_path.name == "index.md":
        rel_path = rel_path.parent
    return rel_path.as_posix()


def compute_target_path(source_file: Path, base_source: Path, base_output: Path) -> Path:
    """Flattens nested index.md file paths into topic-named .md files."""
    rel = source_file.relative_to(base_source)

    if rel == Path("index.md"):
        return base_output / "index.md"

    if rel.name == "index.md":
        return base_output / rel.parent.with_suffix(".md")

    return base_output / rel


def extract_summary(content: str) -> str:
    """Extracts the first descriptive body paragraph from a Markdown document."""
    lines = content.splitlines()
    body_lines = []
    in_yaml = False

    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            in_yaml = not in_yaml
            continue
        if in_yaml or stripped.startswith("#"):
            continue
        if stripped:
            body_lines.append(stripped)
            if len(body_lines) >= 2:
                break

    return " ".join(body_lines)


def build_document_tree(base_source: Path, base_output: Path) -> tuple[dict, dict]:
    """Scans all source documents to build a slug lookup map and a parent-child document tree."""
    slug_map = {}
    doc_tree = {}

    for root, _, files in os.walk(base_source):
        for file in files:
            if file == "index.md":
                source_path = Path(root) / file
                with open(source_path, "r", encoding="utf-8") as f:
                    content = f.read()

                post = frontmatter.loads(content)
                slug = compute_slug(source_path, content)
                target_path = compute_target_path(source_path, base_source, base_output)

                normalized_slug = slug.strip("/").lower()
                rel_output = target_path.relative_to(base_output).as_posix()

                slug_map[normalized_slug] = rel_output

                # Calculate parent slug
                parent_slug = ""
                if "/" in normalized_slug:
                    parent_slug = normalized_slug.rsplit("/", 1)[0]

                doc_tree[normalized_slug] = {
                    "slug": slug,
                    "normalized_slug": normalized_slug,
                    "title": post.metadata.get("title", slug.split("/")[-1]),
                    "summary": extract_summary(post.content),
                    "rel_path": rel_output,
                    "parent_slug": parent_slug,
                    "source_path": source_path,
                    "target_path": target_path,
                }

    return slug_map, doc_tree


def process_all_macros(content: str, current_slug: str, doc_tree: dict) -> str:
    """Expands KumaScript macros and dynamic subpage placeholders into native Markdown."""
    # 1. Experimental Banner Substitution
    exp_banner = (
        "> **Experimental:** This is an experimental technology. "
        "Check the Browser compatibility table carefully before using in production.\n"
    )
    content = re.sub(r"\{\{SeeCompatTable\}\}", exp_banner, content, flags=re.IGNORECASE)

    # 2. Inline Badge Substitutions
    content = re.sub(r"\{\{(?:optional_inline|Optional_Inline)\}\}", "*(Optional)*", content)
    content = re.sub(r"\{\{(?:readonlyinline|ReadOnlyInline)\}\}", "*(Read only)*", content)

    # 3. HTMLElement substitution: {{HTMLElement("iframe")}} -> `<iframe>`
    content = re.sub(r'\{\{HTMLElement\("([^"]+)"\)\}\}', r'`<\1>`', content, flags=re.IGNORECASE)

    # 4. Glossary terms (rendered as plain text)
    content = re.sub(r'\{\{(?:glossary|Glossary)\s*\(\s*"[^"]*"\s*,\s*"([^"]+)"\s*\)\}\}', r'\1', content)
    content = re.sub(r'\{\{(?:glossary|Glossary)\s*\(\s*"([^"]+)"\s*\)\}\}', r'\1', content)

    # 5. Code references with 2 arguments: {{domxref("target", "display")}} or {{HTTPStatus(400, "400 Bad Request")}} -> `display`
    macro_code_2_args = r'\{\{(?:domxref|HTTPStatus|jsxref)\s*\(\s*(?:"[^"]*"|\d+)\s*,\s*"([^"]+)"\s*\)\}\}'
    content = re.sub(macro_code_2_args, r'`\1`', content)

    # 6. Code references with 1 argument: {{domxref("Document.title")}} -> `Document.title`
    macro_code_1_arg = r'\{\{(?:domxref|jsxref)\s*\(\s*"([^"]+)"\s*\)\}\}'
    content = re.sub(macro_code_1_arg, r'`\1`', content)

    # 7. Replace {{Specifications}} macro placeholder
    content = re.sub(
        r"\{\{Specifications\}\}",
        "*Specification defined in the [W3C WebDriver Specification](https://w3c.github.io/webdriver/).*",
        content,
        flags=re.IGNORECASE
    )

    # 8. Dynamic Subpage List Expansion
    norm_current = current_slug.strip("/").lower()
    children = [meta for meta in doc_tree.values() if meta["parent_slug"] == norm_current]
    children.sort(key=lambda x: x["title"].lower())

    if children:
        list_items = [f"* [{child['title']}]({child['rel_path']})" for child in children]
        list_md = "\n".join(list_items) + "\n"

        summary_items = [f"[{child['title']}]({child['rel_path']})\n\n{child['summary']}\n" for child in children]
        summary_md = "\n".join(summary_items)

        content = re.sub(r"\{\{ListSubPages\}\}", list_md, content, flags=re.IGNORECASE)
        content = re.sub(r"\{\{Subpage?sWithSummaries\}\}", summary_md, content, flags=re.IGNORECASE)
    else:
        content = re.sub(r"\{\{ListSubPages\}\}", "", content, flags=re.IGNORECASE)
        content = re.sub(r"\{\{Subpage?sWithSummaries\}\}", "", content, flags=re.IGNORECASE)

    return content


def fetch_bcd_json(category_path: str) -> dict | None:
    """Fetches and caches BCD JSON from the MDN Browser Compatibility Data repository."""
    if category_path in BCD_CACHE:
        return BCD_CACHE[category_path]

    url = f"https://raw.githubusercontent.com/mdn/browser-compat-data/main/{category_path}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "MDN-Release-Script/1.0"})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                BCD_CACHE[category_path] = data
                return data
    except Exception as err:
        print(f"Notice: BCD fetch skipped for '{category_path}': {err}", file=sys.stderr)

    BCD_CACHE[category_path] = None
    return None


def extract_notes_from_entry(entry: dict) -> list[str]:
    """Extracts and normalizes note strings from a BCD support dictionary."""
    if not isinstance(entry, dict) or "notes" not in entry:
        return []

    notes = entry["notes"]
    if isinstance(notes, str):
        return [notes]
    if isinstance(notes, list):
        return [n for n in notes if isinstance(n, str)]
    return []


def resolve_support_with_notes(support_dict: dict, browser: str, feature_desc: str, note_collector: list) -> str:
    """Resolves support version and collects notes with contextual feature descriptions."""
    entry = support_dict.get(browser)

    if entry == "mirror":
        parent_browser = MIRROR_MAP.get(browser)
        if parent_browser:
            entry = support_dict.get(parent_browser)

    if isinstance(entry, list):
        entry = entry[0] if entry else {}

    if not isinstance(entry, dict):
        return "No"

    ver = entry.get("version_added")
    if ver is True:
        version_str = "Yes"
    elif ver is False or ver is None:
        version_str = "No"
    else:
        version_str = str(ver)

    extracted_notes = extract_notes_from_entry(entry)
    if extracted_notes and version_str != "No":
        for note in extracted_notes:
            clean_note = re.sub(r"</?[^>]+>", "", note)
            note_idx = len(note_collector) + 1
            note_collector.append((browser.capitalize(), feature_desc, clean_note))
            version_str += f" [{note_idx}]"

    return version_str


def extract_feature_rows(node: dict, feature_prefix: str = "") -> list:
    """Recursively extracts main feature and sub-parameter nodes containing __compat."""
    rows = []

    if "__compat" in node:
        desc = node["__compat"].get("description")
        if not desc:
            desc = f"`{feature_prefix}`" if feature_prefix else "Base Feature"
        clean_desc = re.sub(r"</?[^>]+>", "", desc)
        rows.append((clean_desc, node["__compat"].get("support", {})))

    for key, value in node.items():
        if key != "__compat" and isinstance(value, dict):
            rows.extend(extract_feature_rows(value, feature_prefix=key))

    return rows


def generate_bcd_table(compat_key: str) -> str:
    """Generates a formatted BCD Markdown table including parameter rows and notes."""
    if not compat_key:
        return "*Browser compatibility data unavailable.*"

    parts = compat_key.split(".")
    if len(parts) < 3:
        return "*Browser compatibility data unavailable.*"

    category_file_path = f"{parts[0]}/{parts[1]}/{parts[2]}"
    bcd_data = fetch_bcd_json(category_file_path)

    if not bcd_data:
        return "*Browser compatibility data available at MDN BCD repository.*"

    current = bcd_data
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            current = None
            break

    if not isinstance(current, dict):
        return "*Browser compatibility data available at MDN BCD repository.*"

    feature_rows = extract_feature_rows(current, feature_prefix=parts[-1])
    if not feature_rows:
        return "*Browser compatibility data available at MDN BCD repository.*"

    browsers = ["chrome", "firefox", "safari", "edge"]
    table_lines = [
        "| Feature | Chrome | Firefox | Safari | Edge |",
        "| :--- | :---: | :---: | :---: | :---: |"
    ]

    note_collector = []

    for desc, support in feature_rows:
        versions = [resolve_support_with_notes(support, b, desc, note_collector) for b in browsers]
        table_lines.append(f"| {desc} | {versions[0]} | {versions[1]} | {versions[2]} | {versions[3]} |")

    if note_collector:
        table_lines.append("\n**Notes:**")
        for idx, (browser_name, feature_desc, note_text) in enumerate(note_collector, 1):
            table_lines.append(f"* **[{idx}] {browser_name} ({feature_desc})**: {note_text}")

    return "\n".join(table_lines) + "\n"


def inject_bcd_compatibility(content: str, compat_key: str) -> str:
    """Replaces {{Compat}} macro placeholders with a generated Markdown table."""
    if "{{Compat}}" in content or "{{compat}}" in content:
        table_md = generate_bcd_table(compat_key)
        content = re.sub(r"\{\{Compat\}\}", table_md, content, flags=re.IGNORECASE)
    return content


def sanitize_frontmatter(post: frontmatter.Post) -> None:
    """Strips non-essential front-matter metadata keys."""
    keys_to_remove = [k for k in post.metadata.keys() if k not in ALLOWED_FRONTMATTER_KEYS]
    for key in keys_to_remove:
        del post.metadata[key]


def rewrite_links(markdown_body: str, slug_map: dict[str, str]) -> str:
    """Rewrites Markdown links to target flattened bundle paths or absolute MDN URLs."""
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def replace_link(match):
        text = match.group(1)
        url = match.group(2)

        parsed = urlparse(url)
        path_raw = parsed.path.strip("/")
        path_lower = path_raw.lower()

        if path_lower.startswith("en-us/docs/"):
            path_lower = path_lower[len("en-us/docs/"):].strip("/")

        anchor = f"#{parsed.fragment}" if parsed.fragment else ""

        if path_lower in slug_map:
            target_file = slug_map[path_lower]
            return f"[{text}]({target_file}{anchor})"

        if parsed.path.startswith("/en-US/docs/"):
            full_url = f"https://developer.mozilla.org{parsed.path}{anchor}"
            return f"[{text}]({full_url})"

        return f"[{text}]({url})"

    return link_pattern.sub(replace_link, markdown_body)


def process_files():
    """Executes the dual-output documentation compilation pipeline."""
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"Source directory not found: {SOURCE_DIR}")

    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    COMPILED_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Building document tree and slug map...")
    slug_map, doc_tree = build_document_tree(SOURCE_DIR, COMPILED_OUTPUT_DIR)

    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file == "index.md":
                source_path = Path(root) / file

                # 1. Copy raw file to RAW_OUTPUT_DIR preserving folder structure
                raw_rel_path = source_path.relative_to(SOURCE_DIR)
                raw_target_path = RAW_OUTPUT_DIR / raw_rel_path
                raw_target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, raw_target_path)

                # 2. Process compiled output file to COMPILED_OUTPUT_DIR
                compiled_target_path = compute_target_path(source_path, SOURCE_DIR, COMPILED_OUTPUT_DIR)
                compiled_target_path.parent.mkdir(parents=True, exist_ok=True)

                with open(source_path, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                post = frontmatter.loads(raw_content)
                slug = compute_slug(source_path, raw_content)
                compat_key = post.metadata.get("browser-compat", "")

                body = post.content

                # Transformation pipeline
                body = process_all_macros(body, slug, doc_tree)
                body = inject_bcd_compatibility(body, compat_key)
                body = rewrite_links(body, slug_map)

                sanitize_frontmatter(post)
                post.content = body

                final_content = frontmatter.dumps(post)

                with open(compiled_target_path, "w", encoding="utf-8") as f:
                    f.write(final_content)

                print(f"Processed: {slug} -> {compiled_target_path}")

    print("Pipeline execution complete.")


if __name__ == "__main__":
    process_files()
    
