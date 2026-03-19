import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

KNOWLEDGE_FILE = "copilot/knowledge.json"


def load_knowledge():
    if not os.path.exists(KNOWLEDGE_FILE):
        return ""

    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [doc["content"] for doc in data]
    return "\n\n".join(texts[:5])  # limita contexto


def ask(question):

    try:
        context = load_knowledge()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Você é um assistente especialista no sistema Rifa Digital.

Use APENAS as informações abaixo para responder:

{context}

Se não souber, diga que não encontrou nos documentos.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Erro:", e)
        return "Erro ao acessar IA."
