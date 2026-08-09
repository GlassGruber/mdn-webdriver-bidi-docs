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

def clean_text(text: str) -> str:
    """Rimuove tutti i tag HTML e la sintassi Bikeshed."""
    text = re.sub(r'<[^>]+>', '', text)             # Rimuove tag HTML (<dfn>, <code>, ecc.)
    text = re.sub(r'\[=([^=]+)=\]', r'\1', text)     # [=term=] -> term
    text = re.sub(r'\{\{([^\}]+)\}\}', r'\1', text) # {{Window}} -> Window
    text = re.sub(r'\{#[^\}]+\}', '', text)         # {#id} -> ""
    return re.sub(r'\s+', ' ', text).strip()

def process_spec(content: str) -> str:
    """Estrae in modo pulito titoli, descrizioni sintetiche e blocchi CDDL."""
    # 1. Scarta la sezione iniziale dei metadati W3C/Bikeshed
    if '# Infrastructure #' in content:
        content = content.split('# Infrastructure #', 1)[1]
    elif '# Protocol #' in content:
        content = content.split('# Protocol #', 1)[1]

    # 2. Divide il contenuto in blocchi basati sulle intestazioni Markdown
    heading_re = re.compile(r'^(#{1,4}\s+.*)$', re.MULTILINE)
    parts = heading_re.split(content)

    output = [
        "# WebDriver BiDi - API & Schema Summary\n",
        "> Sintesi pulita del protocollo W3C per contesto LLM.\n\n"
    ]

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i+1] if i + 1 < len(parts) else ""

        clean_heading = clean_text(heading)

        # Filtra solo i titoli rilevanti per l'API
        if not any(k in clean_heading.lower() for k in ['module', 'command', 'type', 'event', 'protocol']):
            continue

        # Estrae i blocchi CDDL
        cddl_blocks = re.findall(r'<pre\s+class=["\']cddl["\'][^>]*>(.*?)</pre>', body, re.DOTALL | re.IGNORECASE)

        # Estrae la prima frase descrittiva utile
        desc_sentence = ""
        for line in body.splitlines():
            line_str = line.strip()
            if (line_str and not line_str.startswith('<') and 
                not line_str.startswith('Issue:') and 
                not line_str.startswith('Note:') and 
                not line_str.startswith('1.') and 
                not line_str.startswith('*')):
                
                cleaned = clean_text(line_str)
                if cleaned and len(cleaned) > 10:
                    desc_sentence = cleaned
                    break

        # Compone la sezione pulita
        if cddl_blocks or desc_sentence:
            output.append(f"\n{clean_heading}\n")
            if desc_sentence:
                output.append(f"{desc_sentence}\n")
            for cddl in cddl_blocks:
                output.append("```cddl\n" + cddl.strip() + "\n```\n")

    return "\n".join(output)

if __name__ == "__main__":
    print("Download specifica W3C...")
    raw = fetch_spec(SPEC_URL)
    print("Sintesi e pulizia in corso...")
    result = process_spec(raw)
    Path(OUTPUT_FILE).write_text(result, encoding='utf-8')
    print(f"File generato con successo: {OUTPUT_FILE}")
