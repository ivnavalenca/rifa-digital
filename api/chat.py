from flask import Flask, request, jsonify
from copilot.ask import ask

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data["question"]
    answer = ask(question)
    return jsonify({"answer": answer})

app.run(port=5000)
