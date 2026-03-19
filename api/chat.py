import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# 🔥 Corrige o PATH para encontrar /copilot
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 🔥 Import do seu agente
try:
    from copilot.ask import ask
except Exception as e:
    print("Erro ao importar ask:", e)
    ask = None  # fallback

app = Flask(__name__)
CORS(app)

# 🟢 Health check (IMPORTANTE para Render)
@app.route("/")
def home():
    return "API OK 🚀"


# 🤖 Endpoint de chat
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"answer": "Pergunta vazia."})

        # 🔥 Se o ask estiver disponível
        if ask:
            answer = ask(question)
        else:
            answer = "IA indisponível no momento."

        return jsonify({"answer": answer})

    except Exception as e:
        print("Erro no chat:", e)
        return jsonify({"answer": "Erro interno na API."})


# 🚀 Run (Render usa porta 10000)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
