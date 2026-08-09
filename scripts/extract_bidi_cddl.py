import re
import urllib.request
from pathlib import Path

SPEC_URL = "https://github.com/w3c/webdriver-bidi/raw/refs/heads/main/index.bs"
OUTPUT_FILE = "webdriver-bidi-cddl-summary.md"

def fetch_spec(url: str) -> str:
    """Scarica il file di specifica raw dal repository W3C."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def extract_cddl(content: str, output_file: str):
    """Estrae le sezioni e i blocchi CDDL generando un file Markdown sintetico."""
    module_pattern = re.compile(r'##\s+The\s+(\w+)\s+Module\s+##', re.IGNORECASE)
    cddl_block_pattern = re.compile(r'<pre\s+class=["\']cddl["\'][^>]*>(.*?)</pre>', re.DOTALL | re.IGNORECASE)
    
    sections = module_pattern.split(content)
    output = [
        "# WebDriver BiDi - Extracted CDDL & Protocol Schemas\n",
        "> File generato automaticamente dal sorgente ufficiale W3C per contesto LLM.\n\n"
    ]

    # Elaborazione della sezione base
    header_cddls = cddl_block_pattern.findall(sections[0])
    if header_cddls:
        output.append("## Core Protocol Definitions\n")
        for cddl in header_cddls:
            output.append("```cddl\n" + cddl.strip() + "\n```\n")

    # Elaborazione dei moduli
    for i in range(1, len(sections), 2):
        module_name = sections[i]
        module_body = sections[i+1]
        
        cddl_blocks = cddl_block_pattern.findall(module_body)
        if cddl_blocks:
            output.append(f"## Module: {module_name}\n")
            for cddl in cddl_blocks:
                output.append("```cddl\n" + cddl.strip() + "\n```\n")

    Path(output_file).write_text("\n".join(output), encoding='utf-8')
    print(f"Estrazione completata. File generato: {output_file}")

if __name__ == "__main__":
    print("Download della specifica W3C in corso...")
    raw_spec = fetch_spec(SPEC_URL)
    extract_cddl(raw_spec, OUTPUT_FILE)
