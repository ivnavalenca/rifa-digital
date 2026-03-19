import json
import os

print("🤖 Gerando respostas do AI Assistant...")

# 📥 CARREGAR MÉTRICAS
metrics_path = "docs/assets/engineering-metrics.json"

if os.path.exists(metrics_path):
    with open(metrics_path) as f:
        metrics = json.load(f)
else:
    metrics = {}

# 🧠 BASE DE RESPOSTAS
responses = {}

# 📊 STATUS DO PROJETO
issues = metrics.get("open_issues", 0)

if issues < 5:
    health = "🟢 Projeto saudável"
elif issues < 15:
    health = "🟡 Projeto em atenção"
else:
    health = "🔴 Projeto em risco"

responses["status"] = f"{health} (Issues abertas: {issues})"

# 📌 MÉTRICAS
responses["metrics"] = f"""
Documents: {metrics.get('documents', 0)}
Requirements: {metrics.get('requirements', 0)}
User Stories: {metrics.get('user_stories', 0)}
Tests: {metrics.get('tests', 0)}
Services: {metrics.get('services', 0)}
"""

# 🧪 TESTES (exemplo simples)
responses["rf01"] = "Testes que validam RF01: CT001, CT002"
responses["us01"] = "US01 é implementada pelo serviço RifaService"

# 📈 RESUMO
responses["resumo"] = "O sistema possui documentação, testes e arquitetura integrados."

# 📁 GARANTIR PASTA
os.makedirs("docs/assets", exist_ok=True)

# 💾 SALVAR JSON
output_path = "docs/assets/assistant-api.json"

with open(output_path, "w") as f:
    json.dump(responses, f, indent=2)

print("✅ AI responses geradas com sucesso!")
print(json.dumps(responses, indent=2))
