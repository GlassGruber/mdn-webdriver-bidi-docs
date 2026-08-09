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

def process_spec(content: str) -> str:
    # 1. Scarta l'intestazione iniziale dei metadati Bikeshed/W3C fino a Protocol/Infrastructure
    if '# Infrastructure #' in content:
        content = content.split('# Infrastructure #', 1)[1]
    elif '# Protocol #' in content:
        content = content.split('# Protocol #', 1)[1]

    # 2. Scarta i blocchi degli algoritmi di esecuzione interna del browser
    content = re.sub(r'<div\s+algorithm[^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # 3. Divide il file in sezioni basate sulle intestazioni Markdown (#, ##, ###, ####)
    heading_re = re.compile(r'^(#{1,4}\s+.*)$', re.MULTILINE)
    parts = heading_re.split(content)

    output = [
        "# WebDriver BiDi - API & Schema Summary\n",
        "> Sintesi del protocollo W3C con schemi CDDL, note ed issue in formato GitHub Alerts per contesto LLM.\n\n"
    ]

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i+1] if i + 1 < len(parts) else ""

        clean_heading = clean_bikeshed_and_html(heading)

        # Mantiene solo sezioni rilevanti (Moduli, Comandi, Tipi, Eventi, Errori, Protocollo)
        if not any(k in clean_heading.lower() for k in ['module', 'command', 'type', 'event', 'protocol', 'error']):
            continue

        # Estrazione blocchi CDDL
        cddl_blocks = re.findall(r'<pre\s+class=["\']cddl["\'][^>]*>(.*?)</pre>', body, re.DOTALL | re.IGNORECASE)

        # Estrazione paragrafi completi
        paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]

        desc_paragraphs = []
        alerts = []

        for p in paragraphs:
            # Gestione Note -> GitHub Alert [!NOTE]
            if p.lower().startswith('note:') or p.lower().startswith('note ('):
                note_text = clean_bikeshed_and_html(re.sub(r'^note(?:\([^)]+\))?:\s*', '', p, flags=re.IGNORECASE))
                if note_text:
                    formatted_note = "\n> ".join(note_text.splitlines())
                    alerts.append(f"> [!NOTE]\n> {formatted_note}")
                continue

            # Gestione Issue -> GitHub Alert [!IMPORTANT]
            if p.lower().startswith('issue:') or p.lower().startswith('issue('):
                issue_text = clean_bikeshed_and_html(re.sub(r'^issue(?:\([^)]+\))?:\s*', '', p, flags=re.IGNORECASE))
                if issue_text:
                    formatted_issue = "\n> ".join(issue_text.splitlines())
                    alerts.append(f"> [!IMPORTANT]\n> {formatted_issue}")
                continue

            # Salta frammenti di codice o tag residuali
            if p.startswith('{^') or p.startswith('<dl>') or p.startswith('<dt>') or p.startswith('```') or p.startswith('<pre'):
                continue

            # Estrazione descrizione principale del comando/tipo/evento
            cleaned_p = clean_bikeshed_and_html(p)
            if cleaned_p and len(cleaned_p) > 15 and not desc_paragraphs:
                desc_paragraphs.append(cleaned_p)

        # Assemblaggio sezione
        if cddl_blocks or desc_paragraphs or alerts:
            output.append(f"\n{clean_heading}\n")

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
    print("Sintesi ed estrazione con GitHub Alerts in corso...")
    result = process_spec(raw)
    Path(OUTPUT_FILE).write_text(result, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
