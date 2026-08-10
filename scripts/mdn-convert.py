#!/usr/bin/env python3
"""MDN WebDriver Documentation Compiler and Sanitizer.

Processes MDN Markdown source files, fetches compiled HTML payloads from the MDN
Production CDN, converts HTML back to Markdown using markdownify, sanitizes front-matter
metadata, flattens index.md folder structures into topic-named .md files, and normalizes
internal and external Markdown links.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import frontmatter
from markdownify import markdownify as md


# Allowed YAML front-matter keys for LLM context optimization
ALLOWED_FRONTMATTER_KEYS = {"title", "slug", "status"}

SOURCE_DIR = Path("mdn-source/files/en-us/web/webdriver")
OUTPUT_DIR = Path("final-compiled-markdown")


def compute_slug(file_path: Path, raw_content: str) -> str:
    """Extracts the slug from YAML front-matter or computes a fallback from the path."""
    slug_match = re.search(r"^slug:\s*(.*)$", raw_content, re.MULTILINE)
    if slug_match and slug_match.group(1).strip():
        return slug_match.group(1).strip()

    # Fallback based on directory tree structure
    rel_path = file_path.relative_to(Path("mdn-source/files/en-us"))
    if rel_path.name == "index.md":
        rel_path = rel_path.parent
    return rel_path.as_posix()


def compute_target_path(source_file: Path, base_source: Path, base_output: Path) -> Path:
    """Flattens nested index.md file paths into topic-named .md files."""
    rel = source_file.relative_to(base_source)

    # Root index.md remains index.md
    if rel == Path("index.md"):
        return base_output / "index.md"

    # Nested index.md files are flattened to parent_directory_name.md
    if rel.name == "index.md":
        return base_output / rel.parent.with_suffix(".md")

    return base_output / rel


def build_slug_map(base_source: Path, base_output: Path) -> dict[str, str]:
    """Scans source files to build a lookup map of normalized slugs to output file paths."""
    slug_map = {}
    for root, _, files in os.walk(base_source):
        for file in files:
            if file == "index.md":
                source_path = Path(root) / file
                with open(source_path, "r", encoding="utf-8") as f:
                    content = f.read()

                slug = compute_slug(source_path, content)
                target_path = compute_target_path(source_path, base_source, base_output)

                # Normalize slug for case-insensitive lookup (remove slashes)
                normalized_slug = slug.strip("/").lower()
                rel_output = target_path.relative_to(base_output).as_posix()
                slug_map[normalized_slug] = rel_output

    return slug_map


def fetch_compiled_html(slug: str) -> str | None:
    """Fetches compiled JSON payload from the MDN CDN and extracts HTML content sections."""
    json_url = f"https://developer.mozilla.org/en-US/docs/{slug}/index.json"
    req = urllib.request.Request(json_url, headers={"User-Agent": "MDN-Release-Script/1.0"})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                sections = data.get("doc", {}).get("body", [])
                compiled_html = "\n".join(
                    s.get("value") if isinstance(s.get("value"), str) else s.get("value", {}).get("content", "")
                    for s in sections
                )
                return compiled_html
    except Exception as err:
        print(f"Warning: CDN fetch failed for slug '{slug}': {err}", file=sys.stderr)
    return None


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

        # Strip leading 'en-us/docs/' prefix if present
        if path_lower.startswith("en-us/docs/"):
            path_lower = path_lower[len("en-us/docs/"):].strip("/")

        anchor = f"#{parsed.fragment}" if parsed.fragment else ""

        # 1. Match internal bundle slug
        if path_lower in slug_map:
            target_file = slug_map[path_lower]
            return f"[{text}]({target_file}{anchor})"

        # 2. Rewrite external MDN links outside bundle scope
        if parsed.path.startswith("/en-US/docs/"):
            full_url = f"https://developer.mozilla.org{parsed.path}{anchor}"
            return f"[{text}]({full_url})"

        # 3. Third-party URLs remain untouched
        return f"[{text}]({url})"

    return link_pattern.sub(replace_link, markdown_body)


def process_files():
    """Executes the documentation compilation and transformation pipeline."""
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"Source directory not found: {SOURCE_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Building slug lookup dictionary...")
    slug_map = build_slug_map(SOURCE_DIR, OUTPUT_DIR)

    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file == "index.md":
                source_path = Path(root) / file
                target_path = compute_target_path(source_path, SOURCE_DIR, OUTPUT_DIR)

                target_path.parent.mkdir(parents=True, exist_ok=True)

                with open(source_path, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                post = frontmatter.loads(raw_content)
                slug = compute_slug(source_path, raw_content)

                # Fetch compiled HTML content from MDN CDN
                compiled_html = fetch_compiled_html(slug)

                if compiled_html:
                    # Convert HTML to Markdown using ATX headings
                    markdown_body = md(
                        compiled_html,
                        heading_style="ATX",
                        code_language="",
                        bullets="*"
                    )
                else:
                    # Fallback to original raw document body
                    markdown_body = post.content

                # Apply transformations
                sanitize_frontmatter(post)
                transformed_body = rewrite_links(markdown_body, slug_map)
                post.content = transformed_body

                # Write final output file
                final_content = frontmatter.dumps(post)

                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(final_content)

                print(f"Processed: {slug} -> {target_path}")


if __name__ == "__main__":
    process_files()
