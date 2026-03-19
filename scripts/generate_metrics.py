import requests
import json
import os

OWNER = "ivnavalenca"
REPO = "rifa-digital"

url = f"https://api.github.com/repos/{OWNER}/{REPO}"

headers = {}
token = os.getenv("GITHUB_TOKEN")

if token:
    headers["Authorization"] = f"Bearer {token}"

# 📊 Dados principais
repo_data = requests.get(url, headers=headers).json()

# 📌 Issues
issues = requests.get(f"{url}/issues", headers=headers).json()
open_issues = [i for i in issues if "pull_request" not in i]

# 🔀 PRs
prs = requests.get(f"{url}/pulls", headers=headers).json()

# 👥 Contributors
contributors = requests.get(f"{url}/contributors", headers=headers).json()

data = {
    "stars": repo_data.get("stargazers_count", 0),
    "forks": repo_data.get("forks_count", 0),
    "open_issues": len(open_issues),
    "pull_requests": len(prs),
    "contributors": len(contributors)
}

os.makedirs("docs/assets", exist_ok=True)

with open("docs/assets/engineering-metrics.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Metrics geradas com sucesso!")
