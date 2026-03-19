import os
import json

BASE_PATH = "docs/quality"

def count_files(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".md"):
                total += 1
    return total

def main():

    metrics = {
        "test_cases": count_files(f"{BASE_PATH}/design"),
        "test_reports": count_files(f"{BASE_PATH}/execution"),
        "traceability": count_files(f"{BASE_PATH}/traceability"),
        "strategies": count_files(f"{BASE_PATH}/strategy"),
        "process_docs": count_files(f"{BASE_PATH}/process")
    }

    # cálculo simples de "maturidade"
    metrics["quality_score"] = (
        metrics["test_cases"] * 2 +
        metrics["test_reports"] * 2 +
        metrics["traceability"] * 2 +
        metrics["strategies"] +
        metrics["process_docs"]
    )

    os.makedirs("docs/assets", exist_ok=True)

    with open("docs/assets/quality-metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("Quality metrics geradas!")

if __name__ == "__main__":
    main()
