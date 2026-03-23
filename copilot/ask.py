from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
from dotenv import load_dotenv
import os

# 🔑 Carrega variáveis de ambiente
load_dotenv()

client = OpenAI()

# 🔗 URL base do seu site
BASE_URL = "https://ivnavalenca.github.io/rifa-digital/"

# 🧠 embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 🗂️ banco vetorial
db = Chroma(
    persist_directory="copilot/db",
    embedding_function=embeddings
)


def build_links(docs):
    links = []

    for doc in docs:
        source = doc.metadata.get("source", "")

        if "docs/" in source:
            page = source.replace("docs/", "").replace(".md", "")
            url = BASE_URL + page + "/"
            links.append(f"- {url}")

    return "\n".join(set(links))


def ask(question):

    # 🔎 busca semântica
    docs = db.similarity_search(question, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])
    links = build_links(docs)

    prompt = f"""
Você é um especialista no sistema Rifa Digital.

Use o contexto abaixo para responder:

{context}

Regras:
- Responda de forma clara e didática
- Seja objetivo
- Use linguagem simples
- Se possível, explique como um professor
- No final, adicione a seção:

🔗 Referências:
{links}

Pergunta: {question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
