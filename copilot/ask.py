from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

def ask(question):

    db = Chroma(
        persist_directory="db",
        embedding_function=OpenAIEmbeddings()
    )

    docs = db.similarity_search(question, k=3)

    context = "\n".join([d.page_content for d in docs])

    llm = ChatOpenAI(temperature=0)

    prompt = f"""
    Responda com base no contexto abaixo:

    {context}

    Pergunta: {question}
    """

    response = llm.predict(prompt)

    return response


if __name__ == "__main__":
    while True:
        q = input("Pergunta: ")
        print(ask(q))
