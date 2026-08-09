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
    """Pulisce il DOM rimuovendo sezioni escluse, CSS, JS, TOC e formattando note/issue."""
    
    # 1. Rimuove del tutto tag di script, stili e meta-informazioni
    for tag in soup.find_all(['head', 'style', 'script', 'link', 'meta', 'svg', 'noscript']):
        tag.decompose()

    # Rimuove gli attributi style dagli elementi rimanenti
    for tag in soup.find_all(True):
        if 'style' in tag.attrs:
            del tag.attrs['style']

    # 2. Rimuove il Table of Contents (TOC)
    for toc in soup.find_all(id=re.compile(r'^toc$', re.I)):
        toc.decompose()
    for toc in soup.find_all(class_=re.compile(r'^toc$', re.I)):
        toc.decompose()
    for toc in soup.find_all(['nav', 'section'], id=re.compile(r'table-of-contents|toc', re.I)):
        toc.decompose()
    for h in soup.find_all(['h2', 'h3'], string=re.compile(r'Table of Contents|Contents', re.I)):
        parent = h.find_parent(['nav', 'section', 'div']) or h
        parent.decompose()

    # 3. Rimuove elementi prima dell'Abstract usando nodi fratelli (senza ricorsione)
    abstract = soup.find(id='abstract') or soup.find('h2', string=re.compile(r'Abstract', re.I))
    if abstract:
        top_abstract = abstract
        while top_abstract.parent and top_abstract.parent.name not in ['body', 'html', '[document]']:
            top_abstract = top_abstract.parent
        
        for prev in list(top_abstract.previous_siblings):
            if hasattr(prev, 'decompose'):
                prev.decompose()

    # 4. Rimuove 'Status of this document' (#sotd)
    sotd = soup.find(id='sotd') or soup.find('h2', string=re.compile(r'Status of this document', re.I))
    if sotd:
        parent = sotd.find_parent('section') or sotd
        parent.decompose()

    # 5. Rimuove sezioni esplicite da escludere
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

    excluded_heading_patterns = [
        r'8\.\s+Patches', r'9\.\s+Appendices', r'Index', r'References',
        r'CDDL Index', r'Issues Index'
    ]
    for pattern in excluded_heading_patterns:
        for h in soup.find_all(['h2', 'h3', 'h4'], string=re.compile(pattern, re.I)):
            parent = h.find_parent('section') or h
            parent.decompose()

    # 6. Trasforma le Note in GitHub Alerts (> [!NOTE])
    for note in soup.find_all(class_='note'):
        marker = note.find(class_='marker')
        if marker:
            marker.decompose()
        
        note_text = note.get_text().strip()
        formatted_note = "\n> ".join(note_text.splitlines())
        blockquote = soup.new_tag('blockquote')
        blockquote.string = f"[!NOTE]\n{formatted_note}"
        note.replace_with(blockquote)

    # 7. Trasforma le Issue in GitHub Alerts (> [!IMPORTANT]) con numerazione progressiva
    issue_counter = 1
    for issue in soup.find_all(class_='issue'):
        for link in issue.find_all(class_='issue-return'):
            link.decompose()
            
        issue_id = issue.get('id', '')
        issue_label = ""
        
        # Se presente un ID numerico specifico (es. issue-1131), lo estrae
        if issue_id:
            num_match = re.search(r'\d+', issue_id)
            if num_match:
                issue_label = f"Issue #{num_match.group(0)}"

        if not issue_label:
            issue_label = f"Issue #{issue_counter}"
            issue_counter += 1

        issue_text = issue.get_text().strip()
        formatted_issue = "\n> ".join(issue_text.splitlines())
        blockquote = soup.new_tag('blockquote')
        blockquote.string = f"[!IMPORTANT]\n**{issue_label}**: {formatted_issue}"
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
    return markdown_result

if __name__ == "__main__":
    print("Download dell'HTML dalla specifica W3C...")
    html_raw = fetch_html(HTML_URL)
    print("Elaborazione del DOM e conversione in Markdown...")
    md_output = convert_html_to_md(html_raw)
    Path(OUTPUT_FILE).write_text(md_output, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
