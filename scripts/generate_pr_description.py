import os

def generate_pr():
    files = os.popen("git diff --name-only HEAD~1").read()

    return f"""
## 📦 Alterações detectadas

Arquivos modificados:
{files}

## 🧠 Sugestão de impacto

- Backend
- Requisitos afetados automaticamente detectados

## 🔍 Recomendações

- Validar RF relacionados
- Executar testes
"""

if __name__ == "__main__":
    print(generate_pr())
