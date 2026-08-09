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

def transform_and_clean_dom(soup: BeautifulSoup):
    """Pulisce il DOM rimuovendo CSS, JS, TOC, metadati e troncando la specifica dalla Sezione 8 in poi."""
    
    # 1. Rimuove tag di script, stili e meta-informazioni
    for tag in soup.find_all(['head', 'style', 'script', 'link', 'meta', 'svg', 'noscript']):
        tag.decompose()

    for tag in soup.find_all(True):
        if 'style' in tag.attrs:
            del tag.attrs['style']

    # 2. Normalizza i ritorni a capo interni nei paragrafi <p>
    for p in soup.find_all('p'):
        for child in p.find_all(string=True):
            cleaned_str = re.sub(r'[\r\n]+', ' ', child)
            child.replace_with(cleaned_str)

    # 3. Rimuove il Table of Contents (TOC)
    for toc in soup.find_all(id=re.compile(r'^toc$', re.I)):
        toc.decompose()
    for toc in soup.find_all(class_=re.compile(r'^toc$', re.I)):
        toc.decompose()
    for toc in soup.find_all(['nav', 'section'], id=re.compile(r'table-of-contents|toc', re.I)):
        toc.decompose()
    for h in soup.find_all(['h2', 'h3'], string=re.compile(r'Table of Contents|Contents', re.I)):
        parent = h.find_parent(['nav', 'section', 'div']) or h
        parent.decompose()

    # 4. Rimuove la sezione #abstract
    abstract = soup.find(id='abstract') or soup.find('h2', string=re.compile(r'Abstract', re.I))
    if abstract:
        parent_abstract = abstract.find_parent('section') or abstract
        parent_abstract.decompose()

    # 5. Rimuove tutti gli elementi precedenti alla sezione #intro / Introduction
    intro = soup.find(id='intro') or soup.find('h2', string=re.compile(r'Introduction', re.I))
    if intro:
        top_intro = intro
        while top_intro.parent and top_intro.parent.name not in ['body', 'html', '[document]']:
            top_intro = top_intro.parent
        
        for prev in list(top_intro.previous_siblings):
            if hasattr(prev, 'decompose'):
                prev.decompose()

    # 6. Rimuove 'Status of this document' (#sotd)
    sotd = soup.find(id='sotd') or soup.find('h2', string=re.compile(r'Status of this document', re.I))
    if sotd:
        parent = sotd.find_parent('section') or sotd
        parent.decompose()

    # 7. TRONCAMENTO DEFINITIVO: Rimuove la Sezione 8 (Patches) e tutti i nodi successivi fino alla fine del DOM
    patches_elem = (
        soup.find(id='patches') or 
        soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3', 'section'] and 'Patches to Other Specifications' in tag.get_text()) or
        soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3'] and re.search(r'8\.\s+Patches', tag.get_text()))
    )

    if patches_elem:
        top_patches = patches_elem
        while top_patches.parent and top_patches.parent.name not in ['body', 'html', '[document]']:
            top_patches = top_patches.parent
        
        # Elimina tutti i nodi fratelli successivi (Appendices, Index, References, CDDL Index, Issues)
        for next_node in list(top_patches.next_siblings):
            if hasattr(next_node, 'decompose'):
                next_node.decompose()
        
        # Elimina il nodo della Sezione 8 stesso
        top_patches.decompose()

    # 8. Trasforma le Note in GitHub Alerts (> [!NOTE])
    for note in soup.find_all(class_='note'):
        marker = note.find(class_='marker')
        if marker:
            marker.decompose()
        
        note_text = re.sub(r'\s+', ' ', note.get_text()).strip()
        note_text = re.sub(r'^note(?:\([^)]+\))?:\s*', '', note_text, flags=re.IGNORECASE)

        blockquote = soup.new_tag('blockquote')
        p_tag = soup.new_tag('p')
        p_tag.string = f"[!NOTE]\n{note_text}"
        blockquote.append(p_tag)
        note.replace_with(blockquote)

    # 9. Trasforma le Issue in GitHub Alerts (> [!IMPORTANT]) con numerazione progressiva
    issue_counter = 1
    for issue in soup.find_all(class_='issue'):
        for link in issue.find_all(class_='issue-return'):
            link.decompose()
            
        issue_text = re.sub(r'\s+', ' ', issue.get_text()).strip()
        issue_text = re.sub(r'^issue(?:\([^)]+\))?:\s*', '', issue_text, flags=re.IGNORECASE)

        issue_label = f"Issue #{issue_counter}"
        issue_counter += 1

        blockquote = soup.new_tag('blockquote')
        p_tag = soup.new_tag('p')
        p_tag.string = "[!IMPORTANT]\n"

        strong_tag = soup.new_tag('strong')
        strong_tag.string = f"{issue_label}: "

        p_tag.append(strong_tag)
        p_tag.append(issue_text)
        blockquote.append(p_tag)
        issue.replace_with(blockquote)

def convert_html_to_md(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'lxml')
    transform_and_clean_dom(soup)
    
    # Conversione HTML -> Markdown
    markdown_result = md(
        str(soup),
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
    print("Elaborazione del DOM e conversione in Markdown...")
    md_output = convert_html_to_md(html_raw)
    Path(OUTPUT_FILE).write_text(md_output, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
