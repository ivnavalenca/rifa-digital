
# generate_system_atlas.py
#
# Script que analisa a documentação Markdown do projeto e gera um
# resumo estrutural da arquitetura do sistema.
#
# Ele identifica:
# - Serviços (*Service)
# - Entidades de dados (tabelas comuns)
# - Relações simples entre serviços e dados
#
# Saída:
# docs/assets/system-atlas.json

import os
import re
import json

DOCS_PATH = "docs"
OUTPUT_FILE = "docs/assets/system-atlas.json"

services = set()
tables = set()

# tabelas comuns detectadas por padrão
KNOWN_TABLES = [
    "RIFA",
    "NUMERO",
    "PARTICIPANTE",
    "PAGAMENTO",
    "RESULTADO"
]

for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()

                    # detectar serviços
                    services.update(re.findall(r"\b\w+Service\b", text))

                    # detectar tabelas conhecidas
                    for table in KNOWN_TABLES:
                        if table in text:
                            tables.add(table)

            except Exception as e:
                print("Erro lendo:", path, e)

nodes = []
links = []

for s in services:
    nodes.append({
        "id": s,
        "type": "service"
    })

for t in tables:
    nodes.append({
        "id": t,
        "type": "table"
    })

# criar ligações simples serviço → tabela
for s in services:
    for t in tables:
        links.append({
            "source": s,
            "target": t
        })

atlas = {
    "nodes": nodes,
    "links": links
}

os.makedirs("docs/assets", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(atlas, f, indent=2)

print("System atlas generated:", OUTPUT_FILE)
