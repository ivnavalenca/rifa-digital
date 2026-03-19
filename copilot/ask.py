import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(question):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente de engenharia de software."},
                {"role": "user", "content": question}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Erro no OpenAI:", e)
        return "Erro ao acessar IA."
