import requests
import json
import os

# 🔧 CONFIGURAÇÃO
OWNER = "ivnavalenca"
REPO = "rifa-digital"

BASE_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

# 🔐 Token (para evitar limite da API)
headers = {}
token = os.getenv("GITHUB_TOKEN")

if token:
    headers["Authorization"] = f"Bearer {token}"

print("🔎 Coletando dados do GitHub...")

# 📦 Repo
repo = requests.get(BASE_URL, headers=headers).json()

# 🐞 Issues (sem PRs)
issues = requests.get(f"{BASE_URL}/issues?state=open", headers=headers).json()
issues = [i for i in issues if "pull_request" not in i]

# 🔀 Pull Requests
prs = requests.get(f"{BASE_URL}/pulls?state=open", headers=headers).json()

# 👥 Contributors
contributors = requests.get(f"{BASE_URL}/contributors", headers=headers).json()

# 📊 Métricas
data = {
    "stars": repo.get("stargazers_count", 0),
    "forks": repo.get("forks_count", 0),
    "open_issues": len(issues),
    "pull_requests": len(prs),
    "contributors": len(contributors)
}

# 🧠 HEALTH SCORE (bônus)
if data["open_issues"] < 5:
    data["health"] = "🟢 Healthy"
elif data["open_issues"] < 15:
    data["health"] = "🟡 Warning"
else:
    data["health"] = "🔴 Critical"

# 📁 Garantir pasta
os.makedirs("docs/assets", exist_ok=True)

# 💾 Salvar JSON
output_path = "docs/assets/engineering-metrics.json"

with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print("✅ Metrics geradas com sucesso!")
print(json.dumps(data, indent=2))
