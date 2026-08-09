import re
import urllib.request
from pathlib import Path

SPEC_URL = "https://github.com/w3c/webdriver-bidi/raw/refs/heads/main/index.bs"
OUTPUT_FILE = "webdriver-bidi-cddl-summary.md"

def fetch_spec(url: str) -> str:
    """Scarica la specifica W3C grezza."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def clean_bikeshed_and_html(text: str) -> str:
    """Rimuove la sintassi Bikeshed e i tag HTML pulendo gli spazi."""
    text = re.sub(r'\[=([^=]+)=\]', r'\1', text)      # [=term=] -> term
    text = re.sub(r'\{\{([^\}]+)\}\}', r'\1', text)  # {{Window}} -> Window
    text = re.sub(r'\{#[^\}]+\}', '', text)          # {#id} -> ""
    text = re.sub(r'<[^>]+>', '', text)              # Rimuove tag HTML (<dfn>, <code>, <var>)
    return re.sub(r'[ \t]+', ' ', text).strip()

def renumber_algorithm_list(algo_text: str) -> str:
    """Convert le righe '1.' ripetute in un elenco progressivo e annidato."""
    lines = algo_text.splitlines()
    output_lines = []
    
    # Stack per tracciare i contatori di ogni livello di indentazione
    indent_stack = []
    
    for line in lines:
        match = re.match(r'^(\s*)1\.\s+(.*)', line)
        if match:
            indent_spaces = len(match.group(1))
            text_content = clean_bikeshed_and_html(match.group(2))
            
            # Gestione dello stack per i livelli di rientro
            while indent_stack and indent_stack[-1]['indent'] >= indent_spaces:
                indent_stack.pop()
                
            if not indent_stack or indent_stack[-1]['indent'] < indent_spaces:
                new_level = len(indent_stack) + 1
                indent_stack.append({'indent': indent_spaces, 'count': 1, 'level': new_level})
            else:
                indent_stack[-1]['count'] += 1
                
            # Calcolo prefisso numerico (es. 1.2.1 o semplice indentazione)
            level = len(indent_stack)
            current_count = indent_stack[-1]['count']
            
            indent_prefix = "  " * (level - 1)
            output_lines.append(f"{indent_prefix}{current_count}. {text_content}")
        else:
            cleaned = clean_bikeshed_and_html(line)
            if cleaned:
                output_lines.append(cleaned)
                
    return "\n".join(output_lines)

def process_spec(content: str) -> str:
    # 1. Scarta l'intestazione iniziale dei metadati Bikeshed/W3C fino a Protocol/Infrastructure
    if '# Infrastructure #' in content:
        content = content.split('# Infrastructure #', 1)[1]
    elif '# Protocol #' in content:
        content = content.split('# Protocol #', 1)[1]

    # 2. Riconversione dei blocchi <div algorithm> in sezioni leggibili prima della divisione
    def replace_algorithm(match):
        algo_body = match.group(1)
        # Estrazione dell'intestazione dell'algoritmo (es. "To cleanup the session given session:")
        title_match = re.search(r'To\s+<dfn[^>]*>(.*?)</dfn>(.*?):', algo_body, re.IGNORECASE)
        title = ""
        if title_match:
            title = f"**Algorithm: To {clean_bikeshed_and_html(title_match.group(1))}{clean_bikeshed_and_html(title_match.group(2))}**\n"
        
        renumbered = renumber_algorithm_list(algo_body)
        return f"\n\n{title}{renumbered}\n\n"

    # Preserva solo gli algoritmi di alto livello (senza "remote end steps" specifici di comando)
    content_processed = re.sub(r'<div\s+algorithm[^>]*>(.*?)</div>', replace_algorithm, content, flags=re.DOTALL | re.IGNORECASE)

    # 3. Divisione in sezioni gerarchiche
    heading_re = re.compile(r'^(#{1,4}\s+.*)$', re.MULTILINE)
    parts = heading_re.split(content_processed)

    output = [
        "# WebDriver BiDi - API & Schema Summary\n",
        "> Sintesi gerarchica del protocollo W3C per contesto LLM.\n\n"
    ]

    # Contatore gerarchico per la numerazione delle sezioni (H1, H2, H3, H4)
    counters = [0, 0, 0, 0]

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i+1] if i + 1 < len(parts) else ""

        clean_h = clean_bikeshed_and_html(heading)

        # Mantiene sezioni rilevanti (Moduli, Definition, Comandi, Tipi, Eventi, Errori, Protocollo)
        if not any(k in clean_h.lower() for k in ['module', 'definition', 'command', 'type', 'event', 'protocol', 'error']):
            continue

        # Calcolo del livello H1..H4 e aggiornamento numerazione gerarchica
        h_level = len(heading.split()[0])
        counters[h_level - 1] += 1
        for j in range(h_level, len(counters)):
            counters[j] = 0

        section_num = ".".join(str(c) for c in counters[:h_level] if c > 0)
        heading_text = f"{'#' * h_level} {section_num}. {clean_h}"

        # Estrazione blocchi CDDL
        cddl_blocks = re.findall(r'<pre\s+class=["\']cddl["\'][^>]*>(.*?)</pre>', body, re.DOTALL | re.IGNORECASE)

        # Estrazione paragrafi e alert
        paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]

        desc_paragraphs = []
        alerts = []

        for p in paragraphs:
            if p.lower().startswith('note:') or p.lower().startswith('note ('):
                note_text = clean_bikeshed_and_html(re.sub(r'^note(?:\([^)]+\))?:\s*', '', p, flags=re.IGNORECASE))
                if note_text:
                    alerts.append(f"> [!NOTE]\n> {note_text}")
                continue

            if p.lower().startswith('issue:') or p.lower().startswith('issue('):
                issue_text = clean_bikeshed_and_html(re.sub(r'^issue(?:\([^)]+\))?:\s*', '', p, flags=re.IGNORECASE))
                if issue_text:
                    alerts.append(f"> [!IMPORTANT]\n> {issue_text}")
                continue

            if p.startswith('{^') or p.startswith('<dl>') or p.startswith('<dt>') or p.startswith('```') or p.startswith('<pre'):
                continue

            cleaned_p = clean_bikeshed_and_html(p)
            if cleaned_p and len(cleaned_p) > 15 and not desc_paragraphs:
                desc_paragraphs.append(cleaned_p)

        # Assemblaggio sezione
        if cddl_blocks or desc_paragraphs or alerts:
            output.append(f"\n{heading_text}\n")

            if desc_paragraphs:
                output.append(f"{desc_paragraphs[0]}\n")

            if alerts:
                output.append("\n".join(alerts) + "\n")

            for cddl in cddl_blocks:
                output.append("```cddl\n" + cddl.strip() + "\n```\n")

    return "\n".join(output)

if __name__ == "__main__":
    print("Download della specifica W3C...")
    raw = fetch_spec(SPEC_URL)
    print("Sintesi gerarchica ed estrazione in corso...")
    result = process_spec(raw)
    Path(OUTPUT_FILE).write_text(result, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
