import os
import re
import json

DOCS_PATH = "docs/agile"
OUTPUT_FILE = "docs/assets/agile-metrics.json"

user_stories = set()
done = set()
backlog = set()

for root, dirs, files in os.walk(DOCS_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            with open(path, encoding="utf-8") as f:
                text = f.read()

                us = re.findall(r"US\d+", text)

                for u in us:
                    user_stories.add(u)

                if "Done" in text:
                    done.update(us)

                if "Backlog" in text:
                    backlog.update(us)

metrics = {
    "total_user_stories": len(user_stories),
    "done": len(done),
    "backlog": len(backlog)
}

os.makedirs("docs/assets", exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    json.dump(metrics, f, indent=2)

print("Agile metrics generated:", OUTPUT_FILE)
