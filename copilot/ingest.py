import os

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

# 📁 Carrega docs
loader = DirectoryLoader("docs/", glob="**/*.md")
documents = loader.load()

# ✂️ Divide em chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# 🧠 Embeddings
embeddings = OpenAIEmbeddings()

# 💾 Banco vetorial
db = Chroma.from_documents(docs, embeddings, persist_directory="copilot/db")

db.persist()

print("✅ Base vetorial criada com sucesso!")
