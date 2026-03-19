from flask import Flask, request, jsonify
from flask_cors import CORS
from copilot.ask import ask

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")
    
    answer = ask(question)
    
    return jsonify({"answer": answer})

@app.route("/")
def home():
    return "API OK 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
