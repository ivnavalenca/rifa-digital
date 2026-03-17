# agent.py
#
# Engineering Agent for the Rifa Digital project.
#
# This script performs simple engineering analysis by scanning the
# documentation and identifying relationships between:
# - Requirements (RF)
# - User Stories (US)
# - Test Cases (CT)
# - Services (*Service)
#
# It also detects possible gaps such as:
# - Requirements without tests
# - Services without references in documentation
#
# Output:
# prints analysis in the console (can be used in CI/CD pipelines)

import os
import re

DOCS_PATH = "docs"

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
                print("Error reading:", path, e)


print("\nEngineering Analysis")
print("---------------------")

print("Requirements:", len(requirements))
print("User Stories:", len(user_stories))
print("Tests:", len(tests))
print("Services:", len(services))

# Detect requirements without tests
missing_tests = []

for r in requirements:
    found = False
    for t in tests:
        if r.replace("RF", "CT") in t:
            found = True

    if not found:
        missing_tests.append(r)

print("\nRequirements without mapped tests:")

if not missing_tests:
    print("None")
else:
    for r in missing_tests:
        print("-", r)

print("\nDetected Services:")
for s in services:
    print("-", s)

print("\nEngineering Agent finished.")
