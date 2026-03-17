
# auto_architect.py
#
# Auto Architect Agent
# --------------------
# This script analyzes the documentation of the project and tries to infer
# architectural components such as:
# - Services (*Service)
# - Database tables
# - Requirements (RF)
#
# It prints suggestions for improving the architecture.

import os
import re

DOCS_PATH = "docs"

services = set()
tables = set()
requirements = set()

for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()

                    services.update(re.findall(r"\b\w+Service\b", text))
                    requirements.update(re.findall(r"RF\d+", text))

                    # detect common table names
                    tables.update(
                        re.findall(
                            r"\bRIFA\b|\bNUMERO\b|\bPARTICIPANTE\b|\bPAGAMENTO\b|\bRESULTADO\b",
                            text,
                        )
                    )

            except Exception as e:
                print("Error reading:", path, e)


print("\nAuto Architect Analysis")
print("------------------------")

print("Detected Services:", len(services))
for s in services:
    print("-", s)

print("\nDetected Tables:", len(tables))
for t in tables:
    print("-", t)

print("\nDetected Requirements:", len(requirements))

print("\nArchitecture Suggestions")
print("------------------------")

if len(services) <= 2:
    print("- Consider splitting responsibilities into more services.")

if "PagamentoService" not in services:
    print("- Consider creating a PagamentoService to isolate payment logic.")

if "SorteioService" not in services:
    print("- Consider adding a SorteioService to manage raffle draws.")

if not tables:
    print("- No database tables detected in documentation.")

print("\nAuto Architect finished.")
