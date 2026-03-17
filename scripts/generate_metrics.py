
# generate_metrics.py
#
# Script que gera métricas simples de engenharia a partir da documentação
# do projeto. Ele conta:
# - Requisitos (RF)
# - User Stories (US)
# - Casos de Teste (CT)
# - Serviços (*Service)
#
# Saída:
# docs/assets/engineering-metrics.json

import os
import re
import json

DOCS_PATH = "docs"
OUTPUT_FILE = "docs/assets/engineering-metrics.json"

requirements = set()
user_stories = set()
tests = set()
services = set()
documents = 0

for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            documents += 1
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

metrics = {
    "documents": documents,
    "requirements": len(requirements),
    "user_stories": len(user_stories),
    "tests": len(tests),
    "services": len(services)
}

os.makedirs("docs/assets", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

print("Engineering metrics generated:", OUTPUT_FILE)
