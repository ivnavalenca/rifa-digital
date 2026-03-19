import os
from openai import OpenAI

# Inicializa cliente com a chave do ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente do sistema Rifa Digital e responde de forma clara e objetiva."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Erro no ask.py:", e)
        return "Erro ao acessar IA."
