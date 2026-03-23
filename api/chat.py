from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import traceback

# 🔑 carrega .env
load_dotenv()

app = Flask(__name__)
CORS(app)

try:
    from copilot.ask import ask
except Exception as e:
    print("❌ Erro ao importar ask:")
    traceback.print_exc()
    ask = None

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question")

    if not ask:
        return jsonify({"answer": "Erro interno: IA não carregada."})

    try:
        answer = ask(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Erro ao acessar IA: {str(e)}"})

@app.route("/")
def home():
    return "API Rifa Digital rodando 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
