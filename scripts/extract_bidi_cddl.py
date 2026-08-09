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

def sanitize_text(text: str) -> str:
    """Rimuove la sintassi di markup Bikeshed dal testo descrittivo."""
    text = re.sub(r'\[=([^=]+)=\]', r'\1', text)  # [=term=] -> term
    text = re.sub(r'\{\{([^\}]+)\}\}', r'\1', text)  # {{Window}} -> Window
    text = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', text)  # <a>link</a> -> link
    return text.strip()

def process_spec(content: str) -> str:
    """Estrae titoli, descrizioni sintetiche e blocchi CDDL ignorando gli algoritmi interni."""
    # Rimuove tutti i blocchi algoritmici del browser (rumore principale)
    content_clean = re.sub(r'<div\s+algorithm[^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    lines = content_clean.splitlines()
    output = [
        "# WebDriver BiDi - Extracted Specification & CDDL Schemas\n",
        "> Sintesi automatizzata per contesto LLM (Descrizioni + Schemi CDDL).\n\n"
    ]

    in_cddl = False
    current_cddl = []
    current_desc = []

    for line in lines:
        # Tracciamento dei titoli dei moduli e dei comandi/eventi (es. ### o ####)
        if line.startswith('#'):
            heading_level = len(line.split()[0])
            heading_text = line.lstrip('#').strip()
            
            # Pulisce eventuali ID Bikeshed nei titoli {#id}
            heading_text = re.sub(r'\{#[^\}]+\}', '', heading_text).strip()

            if heading_level in [2, 3, 4]:
                output.append(f"\n{'#' * heading_level} {heading_text}\n")
            continue

        # Inizio blocco CDDL
        if re.search(r'<pre\s+class=["\']cddl["\']', line, re.IGNORECASE):
            in_cddl = True
            current_cddl = []
            # Scrive l'eventuale descrizione accumulata prima del blocco CDDL
            if current_desc:
                desc_text = " ".join(current_desc).strip()
                if desc_text:
                    output.append(f"{sanitize_text(desc_text)}\n")
                current_desc = []
            continue

        # Fine blocco CDDL
        if in_cddl and '</pre>' in line:
            in_cddl = False
            output.append("```cddl\n" + "\n".join(current_cddl).strip() + "\n```\n")
            current_cddl = []
            continue

        # Accumulo contenuto CDDL
        if in_cddl:
            current_cddl.append(line)
            continue

        # Accumulo testo descrittivo (escludendo tag HTML e righe vuote)
        trimmed = line.strip()
        if trimmed and not trimmed.startswith('<') and not trimmed.startswith(';') and not trimmed.startswith('Note:'):
            current_desc.append(trimmed)

    return "\n".join(output)

if __name__ == "__main__":
    print("Download della specifica W3C...")
    raw_spec = fetch_spec(SPEC_URL)
    print("Elaborazione e sintesi in corso...")
    result_md = process_spec(raw_spec)
    Path(OUTPUT_FILE).write_text(result_md, encoding='utf-8')
    print(f"Completato. File generato: {OUTPUT_FILE}")
