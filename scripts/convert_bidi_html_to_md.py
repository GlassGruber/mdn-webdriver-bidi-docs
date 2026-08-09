import re
import urllib.request
from bs4 import BeautifulSoup
from markdownify import markdownify as md

HTML_URL = "https://w3c.github.io/webdriver-bidi/"
OUTPUT_FILE = "webdriver-bidi-spec-full.md"

def fetch_html(url: str) -> str:
    """Scarica l'HTML della specifica W3C."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def transform_and_clean_dom(soup: BeautifulSoup):
    """Pulisce il DOM rimuovendo le sezioni indesiderate e convertendo note/issue."""
    
    # 1. Rimuove la sezione 'Status of this document'
    sotd = soup.find(id='sotd') or soup.find('h2', string=re.compile(r'Status of this document', re.I))
    if sotd:
        parent = sotd.find_parent('section') or sotd
        parent.decompose()

    # 2. Rimuove sezioni esplicite da escludere tramite ID o intestazione
    excluded_ids = [
        'patches', 'appendices', 'index', 'references', 
        'cddl-index', 'issues-index', 'terms-defined-by-this-specification',
        'terms-defined-by-reference', 'normative-references', 'non-normative-references'
    ]
    
    for exc_id in excluded_ids:
        elem = soup.find(id=exc_id)
        if elem:
            parent = elem.find_parent('section') or elem
            parent.decompose()

    # Rimuove intestazioni corrispondenti a sezioni da escludere
    excluded_heading_patterns = [
        r'8\.\s+Patches', r'9\.\s+Appendices', r'Index', r'References',
        r'CDDL Index', r'Issues Index'
    ]
    for pattern in excluded_heading_patterns:
        for h in soup.find_all(['h2', 'h3', 'h4'], string=re.compile(pattern, re.I)):
            parent = h.find_parent('section') or h
            parent.decompose()

    # 3. Trasforma le Note in GitHub Alerts (> [!NOTE])
    for note in soup.find_all(class_='note'):
        # Rimuove l'etichetta "Note:" duplicate se presente nel marker
        marker = note.find(class_='marker')
        if marker:
            marker.decompose()
        
        note_text = note.get_text().strip()
        # Sostituisce il contenuto HTML del nodo con una struttura blockquote
        blockquote = soup.new_tag('blockquote')
        blockquote.string = f"[!NOTE]\n{note_text}"
        note.replace_with(blockquote)

    # 4. Trasforma le Issue in GitHub Alerts (> [!IMPORTANT])
    for issue in soup.find_all(class_='issue'):
        # Rimuove eventuali link di ritorno
        for link in issue.find_all(class_='issue-return'):
            link.decompose()
            
        issue_text = issue.get_text().strip()
        blockquote = soup.new_tag('blockquote')
        blockquote.string = f"[!IMPORTANT]\nISSUE: {issue_text}"
        issue.replace_with(blockquote)

    # 5. Rimuove elementi prima dell'Abstract / Introduzione
    abstract = soup.find(id='abstract') or soup.find('h2', string=re.compile(r'Abstract', re.I))
    if abstract:
        # Rimuove tutti i fratelli precedenti al blocco Abstract
        parent_container = abstract.parent
        for prev in list(abstract.find_all_previous()):
            if prev.parent == parent_container and prev != abstract:
                prev.decompose()

def convert_html_to_md(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    transform_and_clean_dom(soup)
    
    # Conversione HTML pulito -> Markdown
    markdown_result = md(
        str(soup),
        heading_style="ATX",
        code_language="cddl",
        strip=['script', 'style']
    )
    
    # Pulizia righe vuote multiple
    markdown_result = re.sub(r'\n{3,}', '\n\n', markdown_result)
    return markdown_result

if __name__ == "__main__":
    print("Download dell'HTML dalla specifica W3C...")
    html_raw = fetch_html(HTML_URL)
    print("Elaborazione del DOM e conversione in Markdown...")
    md_output = convert_html_to_md(html_raw)
    Path(OUTPUT_FILE).write_text(md_output, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
