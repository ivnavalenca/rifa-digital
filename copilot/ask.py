import json
from openai import OpenAI

client = OpenAI()

def ask(question):

    try:
        with open("copilot/knowledge.json") as f:
            knowledge = json.load(f)
    except:
        knowledge = {}

    context = json.dumps(knowledge)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Use este contexto para responder:\n{context}"},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
