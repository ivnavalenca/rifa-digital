
# ask.py
#
# Simple CLI interface to query the Engineering Knowledge Graph
# generated from the documentation.
#
# It reads:
# docs/assets/knowledge-graph.json
#
# and allows basic queries about relationships between nodes.

import json

GRAPH_FILE = "docs/assets/knowledge-graph.json"


def load_graph():
    try:
        with open(GRAPH_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading graph:", e)
        return {"nodes": [], "links": []}


def find_links(graph, query):
    results = []

    for link in graph["links"]:
        if query in link["source"] or query in link["target"]:
            results.append(link)

    return results


def main():
    graph = load_graph()

    print("Engineering Copilot CLI")
    print("-----------------------")
    print("Type a node name (RF, US, CT, Service) or 'exit' to quit.
")

    while True:
        q = input("Query: ").strip()

        if q.lower() in ["exit", "quit"]:
            break

        results = find_links(graph, q)

        if not results:
            print("No relationships found.
")
        else:
            print("Relationships:")
            for r in results:
                print(" -", r["source"], "->", r["target"])
            print()


if __name__ == "__main__":
    main()
