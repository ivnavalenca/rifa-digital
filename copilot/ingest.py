import os

from langchain_community.document_loaders import DirectoryLoader
from langchain-text-splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# 📂 Caminhos
DOCS_PATH = "docs/"
DB_PATH = "copilot/db"

print("📂 Carregando documentos...")

# 🔎 Carrega todos os .md do projeto
loader = DirectoryLoader(DOCS_PATH, glob="**/*.md")
documents = loader.load()

print(f"📄 {len(documents)} documentos carregados")

# ❗ Validação
if len(documents) == 0:
    print("❌ Nenhum documento encontrado em docs/")
    exit(1)

# ✂️ Divide em pedaços (chunks)
splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

print(f"✂️ {len(docs)} chunks criados")

# 🧠 Embeddings
print("🧠 Gerando embeddings...")

if not os.getenv("OPENAI_API_KEY"):
    print("❌ OPENAI_API_KEY não encontrada!")
    exit(1)

embeddings = OpenAIEmbeddings()

# 🗑️ Limpa DB antigo (evita conflito)
if os.path.exists(DB_PATH):
    import shutil
    shutil.rmtree(DB_PATH)
    print("🗑️ DB antigo removido")

# 💾 Cria banco vetorial
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory=DB_PATH
)

db.persist()

print("✅ Banco vetorial criado com sucesso em:", DB_PATH)
