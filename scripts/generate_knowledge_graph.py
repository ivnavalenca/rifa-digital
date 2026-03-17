
# generate_knowledge_graph.py
#
# Script que gera um Knowledge Graph simples a partir da documentação
# Markdown do projeto. Ele identifica:
# - Requisitos (RF)
# - User Stories (US)
# - Casos de Teste (CT)
# - Serviços (*Service)
#
# Saída:
# docs/assets/images/knowledge-graph.json

import os
import re
import json

DOCS_PATH = "docs"
OUTPUT_FILE = "docs/assets/images/knowledge-graph.json"

requirements = set()
user_stories = set()
tests = set()
services = set()

for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()

                    requirements.update(re.findall(r"RF\d+", text))
                    user_stories.update(re.findall(r"US\d+", text))
                    tests.update(re.findall(r"CT\d+", text))
                    services.update(re.findall(r"\b\w+Service\b", text))

            except Exception as e:
                print("Erro lendo:", path, e)

nodes = []
links = []

for r in requirements:
    nodes.append({"id": r, "type": "requirement"})

for u in user_stories:
    nodes.append({"id": u, "type": "user_story"})

for t in tests:
    nodes.append({"id": t, "type": "test"})

for s in services:
    nodes.append({"id": s, "type": "service"})

# Liga requisitos → user stories
for r in requirements:
    for u in user_stories:
        links.append({"source": r, "target": u})

# Liga user stories → serviços
for u in user_stories:
    for s in services:
        links.append({"source": u, "target": s})

# Liga requisitos → testes
for r in requirements:
    for t in tests:
        links.append({"source": r, "target": t})

graph = {
    "nodes": nodes,
    "links": links
}

os.makedirs("docs/assets/images", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(graph, f, indent=2)

print("Knowledge graph generated:", OUTPUT_FILE)
