
# generate_traceability_graph.py
#
# Script que gera um grafo de rastreabilidade entre:
# - Requisitos (RF)
# - User Stories (US)
# - Casos de Teste (CT)
#
# Saída:
# docs/assets/traceability-graph.json

import os
import re
import json

DOCS_PATH = "docs"
OUTPUT_FILE = "docs/assets/traceability-graph.json"

requirements = set()
user_stories = set()
tests = set()

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

# criar ligações simples
for r in requirements:
    for u in user_stories:
        links.append({
            "source": r,
            "target": u
        })

for u in user_stories:
    for t in tests:
        links.append({
            "source": u,
            "target": t
        })

graph = {
    "nodes": nodes,
    "links": links
}

os.makedirs("docs/assets", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(graph, f, indent=2)

print("Traceability graph generated:", OUTPUT_FILE)
