from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔥 Import seguro do ask
try:
    from copilot.ask import ask
except Exception as e:
    print("Erro ao importar ask:", e)
    ask = None


@app.route("/", methods=["GET"])
def home():
    return "API do Chat está rodando 🚀"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        # valida entrada
        if not data or "question" not in data:
            return jsonify({"answer": "Pergunta não fornecida"}), 400

        question = data["question"]

        # verifica se IA está disponível
        if ask is None:
            return jsonify({"answer": "IA indisponível no momento."})

        # chama IA
        answer = ask(question)

        return jsonify({"answer": answer})

    except Exception as e:
        print("Erro no /chat:", e)
        return jsonify({"answer": "Erro interno no servidor."}), 500


# 🔥 IMPORTANTE para Render
if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
