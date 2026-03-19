import os
import json

DOCS_PATH = "docs"
OUTPUT_FILE = "copilot/knowledge.json"

def load_documents():
    docs = []

    for root, _, files in os.walk(DOCS_PATH):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                docs.append({
                    "file": path,
                    "content": content[:2000]  # evita textos enormes
                })

    return docs


def main():
    docs = load_documents()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)

    print(f"{len(docs)} documentos ingeridos")


if __name__ == "__main__":
    main()
