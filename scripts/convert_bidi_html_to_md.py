import datetime
import re
import sys
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Incremento del limite di ricorsione per alberi DOM complessi
sys.setrecursionlimit(25000)

HTML_URL = "https://www.w3.org/TR/2026/WD-webdriver-bidi-20260629"
OUTPUT_FILE = "webdriver-bidi-spec-full.md"

def fetch_html(url: str) -> str:
    """Scarica l'HTML della specifica W3C."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def transform_and_clean_main(main_soup: BeautifulSoup) -> BeautifulSoup:
    """Pulisce ed elabora esclusivamente il contenuto presente all'interno del nodo <main>."""
    
    # 1. Rimuove tag non necessari all'interno di <main>
    for tag in main_soup.find_all(['style', 'script', 'link', 'meta', 'svg', 'noscript']):
        tag.decompose()

    for tag in main_soup.find_all(True):
        if 'style' in tag.attrs:
            del tag.attrs['style']

    # 2. Normalizza i ritorni a capo interni nei paragrafi <p>
    for p in main_soup.find_all('p'):
        for child in p.find_all(string=True):
            cleaned_str = re.sub(r'[\r\n]+', ' ', child)
            child.replace_with(cleaned_str)

    # 3. Rimuove il Table of Contents (TOC) se presente dentro <main>
    for toc in main_soup.find_all(id=re.compile(r'^toc$', re.I)):
        toc.decompose()
    for toc in main_soup.find_all(class_=re.compile(r'^toc$', re.I)):
        toc.decompose()
    for toc in main_soup.find_all(['nav', 'section'], id=re.compile(r'table-of-contents|toc', re.I)):
        toc.decompose()

    # 4. Rimuove #abstract e #sotd se presenti dentro <main>
    for exc_id in ['abstract', 'sotd']:
        elem = main_soup.find(id=exc_id)
        if elem:
            parent = elem.find_parent('section') or elem
            parent.decompose()

    # 5. Rimuove Sezione 8 (Patches) o sezioni finali da escludere se presenti dentro <main>
    excluded_ids = [
        'patches', 'appendices', 'index', 'references', 
        'cddl-index', 'issues-index', 'terms-defined-by-this-specification',
        'terms-defined-by-reference', 'normative-references', 'non-normative-references'
    ]
    for exc_id in excluded_ids:
        elem = main_soup.find(id=exc_id)
        if elem:
            # Rimuove l'elemento e tutti i nodi fratelli successivi dentro <main>
            for next_sibling in list(elem.next_siblings):
                if hasattr(next_sibling, 'decompose'):
                    next_sibling.decompose()
            elem.decompose()

    # 6. Trasforma le Note in GitHub Alerts (> [!NOTE])
    for note in main_soup.find_all(class_='note'):
        marker = note.find(class_='marker')
        if marker:
            marker.decompose()
        
        note_text = re.sub(r'\s+', ' ', note.get_text()).strip()
        note_text = re.sub(r'^note(?:\([^)]+\))?:\s*', '', note_text, flags=re.IGNORECASE)

        blockquote = main_soup.new_tag('blockquote')
        p_tag = main_soup.new_tag('p')
        p_tag.append(f"[!NOTE]\n{note_text}")
        blockquote.append(p_tag)
        note.replace_with(blockquote)

    # 7. Trasforma le Issue in GitHub Alerts (> [!IMPORTANT]) con numerazione progressiva e tag strong
    issue_counter = 1
    for issue in main_soup.find_all(class_='issue'):
        for link in issue.find_all(class_='issue-return'):
            link.decompose()
            
        issue_text = re.sub(r'\s+', ' ', issue.get_text()).strip()
        issue_text = re.sub(r'^issue(?:\([^)]+\))?:\s*', '', issue_text, flags=re.IGNORECASE)

        issue_label = f"Issue #{issue_counter}"
        issue_counter += 1

        blockquote = main_soup.new_tag('blockquote')
        p_tag = main_soup.new_tag('p')
        p_tag.append("[!IMPORTANT]\n")

        strong_tag = main_soup.new_tag('strong')
        strong_tag.string = f"{issue_label}: "

        p_tag.append(strong_tag)
        p_tag.append(issue_text)
        blockquote.append(p_tag)
        issue.replace_with(blockquote)

    return main_soup

def convert_html_to_md(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Isola esclusivamente l'elemento <main>
    main_node = soup.find('main') or soup.find(attrs={'role': 'main'}) or soup.find('body')
    
    # Crea un sotto-DOM contenente solo <main>
    main_soup = BeautifulSoup(str(main_node), 'lxml')
    
    # Elabora il sotto-DOM
    cleaned_main = transform_and_clean_main(main_soup)
    
    # Conversione HTML -> Markdown
    markdown_result = md(
        str(cleaned_main),
        heading_style="ATX",
        code_language="cddl",
        strip=['script', 'style', 'head', 'link', 'meta', 'noscript']
    )
    
    # Pulizia righe vuote multiple
    markdown_result = re.sub(r'\n{3,}', '\n\n', markdown_result)
    
    # Inserimento Front Matter YAML
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    front_matter = (
        "---\n"
        f"generated_at: '{now_utc}'\n"
        f"source_url: '{HTML_URL}'\n"
        "---\n\n"
    )
    
    return front_matter + markdown_result

if __name__ == "__main__":
    print("Download dell'HTML dalla specifica W3C...")
    html_raw = fetch_html(HTML_URL)
    print("Isolamento di <main> e conversione in Markdown...")
    md_output = convert_html_to_md(html_raw)
    Path(OUTPUT_FILE).write_text(md_output, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
