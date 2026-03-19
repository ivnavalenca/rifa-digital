import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

print("📥 Iniciando ingestão dos documentos...")

# 📂 Pasta de documentação
DOCS_PATH = "docs"

# 📦 Carregar arquivos Markdown
loader = DirectoryLoader(DOCS_PATH, glob="**/*.md")
documents = loader.load()

print(f"📄 {len(documents)} documentos carregados")

# ✂️ Dividir em chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"✂️ {len(chunks)} chunks gerados")

# 🔐 API Key (OpenAI)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY não configurada")

# 🧠 Criar embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# 💾 Criar banco vetorial
DB_PATH = "copilot/db"

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory=DB_PATH
)

db.persist()

print("✅ Base vetorial criada com sucesso!")
print(f"📍 Local: {DB_PATH}")
