import re
import sys
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Incremento del limite di ricorsione per alberi DOM complessi
sys.setrecursionlimit(25000)

HTML_URL = "https://w3c.github.io/webdriver-bidi/"
OUTPUT_FILE = "webdriver-bidi-spec-full.md"

def fetch_html(url: str) -> str:
    """Scarica l'HTML della specifica W3C."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def transform_and_clean_dom(soup: BeautifulSoup):
    """Pulisce il DOM rimuovendo le sezioni indesiderate e convertendo note/issue."""
    
    # 1. Rimuove elementi prima dell'Abstract usando nodi fratelli (evita ricorsione)
    abstract = soup.find(id='abstract') or soup.find('h2', string=re.compile(r'Abstract', re.I))
    if abstract:
        top_abstract = abstract
        # Risale fino al contenitore di primo livello (figlio diretto di body/html)
        while top_abstract.parent and top_abstract.parent.name not in ['body', 'html', '[document]']:
            top_abstract = top_abstract.parent
        
        # Elimina i fratelli precedenti in modo piatto senza traversata ricorsiva
        for prev in list(top_abstract.previous_siblings):
            if hasattr(prev, 'decompose'):
                prev.decompose()

    # 2. Rimuove la sezione 'Status of this document'
    sotd = soup.find(id='sotd') or soup.find('h2', string=re.compile(r'Status of this document', re.I))
    if sotd:
        parent = sotd.find_parent('section') or sotd
        parent.decompose()

    # 3. Rimuove sezioni esplicite da escludere tramite ID
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

    # 4. Trasforma le Note in GitHub Alerts (> [!NOTE])
    for note in soup.find_all(class_='note'):
        marker = note.find(class_='marker')
        if marker:
            marker.decompose()
        
        note_text = note.get_text().strip()
        formatted_note = "\n> ".join(note_text.splitlines())
        blockquote = soup.new_tag('blockquote')
        blockquote.string = f"[!NOTE]\n{formatted_note}"
        note.replace_with(blockquote)

    # 5. Trasforma le Issue in GitHub Alerts (> [!IMPORTANT])
    for issue in soup.find_all(class_='issue'):
        for link in issue.find_all(class_='issue-return'):
            link.decompose()
            
        issue_text = issue.get_text().strip()
        formatted_issue = "\n> ".join(issue_text.splitlines())
        blockquote = soup.new_tag('blockquote')
        blockquote.string = f"[!IMPORTANT]\nISSUE: {formatted_issue}"
        issue.replace_with(blockquote)

def convert_html_to_md(html_content: str) -> str:
    # Uso del parser 'lxml' per prestazioni e tolleranza superiori
    soup = BeautifulSoup(html_content, 'lxml')
    transform_and_clean_dom(soup)
    
    # Conversione HTML -> Markdown
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
