from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from openai import OpenAI

client = OpenAI()

# 🔍 Carrega base vetorial
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="copilot/db", embedding_function=embeddings)

def ask(question):

    # 🔎 Busca semântica
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    # 🤖 IA responde com contexto
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Responda baseado no contexto abaixo:\n{context}"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content
