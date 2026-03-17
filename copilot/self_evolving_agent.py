
# self_evolving_agent.py
#
# Self Evolving Engineering Agent
# --------------------------------
# This agent scans the documentation and tries to improve the engineering
# artifacts automatically. It currently detects:
#
# - Requirements (RF)
# - Test cases (CT)
#
# If a requirement does not have a corresponding test case, the agent
# automatically generates a basic test case file.
#
# Generated files:
# docs/testing/cases/CT_auto_RFxx.md

import os
import re

DOCS_PATH = "docs"
TEST_OUTPUT_PATH = "docs/testing/cases"

requirements = set()
tests = set()

# Scan documentation
for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()

                    requirements.update(re.findall(r"RF\d+", text))
                    tests.update(re.findall(r"CT\d+", text))

            except Exception as e:
                print("Error reading:", path, e)


# Detect requirements without tests
missing = []

for r in requirements:
    expected = r.replace("RF", "CT")

    found = False
    for t in tests:
        if expected in t:
            found = True
            break

    if not found:
        missing.append(r)


print("\nSelf Evolving Agent Analysis")
print("--------------------------------")
print("Requirements detected:", len(requirements))
print("Tests detected:", len(tests))

if not missing:
    print("All requirements already have associated tests.")
else:
    print("\nMissing tests for requirements:")
    for r in missing:
        print("-", r)


# Generate missing tests
os.makedirs(TEST_OUTPUT_PATH, exist_ok=True)

for r in missing:

    filename = f"CT_auto_{r}.md"
    filepath = os.path.join(TEST_OUTPUT_PATH, filename)

    content = f"""
# Caso de Teste Automático

Requisito relacionado: {r}

## Cenário

Validar comportamento do sistema relacionado ao requisito.

## Passos

1. Preparar dados necessários
2. Executar funcionalidade do sistema
3. Verificar resultado esperado

## Resultado Esperado

O sistema atende corretamente ao requisito {r}.
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print("Generated test:", filepath)

print("\nSelf evolving agent finished.")
