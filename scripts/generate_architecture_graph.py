
# generate_architecture_graph.py
#
# Script responsável por gerar um grafo da arquitetura do sistema
# a partir da documentação Markdown do projeto.
#
# Saída:
# docs/assets/images/architecture-graph.json

import os
import re
import json

DOCS_PATH = "docs"
OUTPUT_FILE = "docs/assets/images/architecture-graph.json"

services = set()
tables = set()

for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()

                    # Detecta serviços
                    services.update(re.findall(r"\b\w+Service\b", text))

                    # Detecta tabelas comuns do sistema
                    tables.update(
                        re.findall(r"\bRIFA\b|\bNUMERO\b|\bRESULTADO\b|\bPAGAMENTO\b", text)
                    )

            except Exception as e:
                print("Erro lendo:", path, e)

nodes = []
links = []

# Criar nós de serviços
for s in services:
    nodes.append({
        "id": s,
        "type": "service"
    })

# Criar nós de tabelas
for t in tables:
    nodes.append({
        "id": t,
        "type": "table"
    })

# Criar ligações simples entre serviços e tabelas
for s in services:
    for t in tables:
        links.append({
            "source": s,
            "target": t
        })

graph = {
    "nodes": nodes,
    "links": links
}

os.makedirs("docs/assets/images", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(graph, f, indent=2)

print("Architecture graph generated:", OUTPUT_FILE)
