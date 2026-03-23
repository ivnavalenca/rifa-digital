import os
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# 📂 Caminhos
DOCS_PATH = "docs/"
DB_PATH = "copilot/db"

print("📂 Carregando documentos...")

documents = []

# 🔎 Carrega todos os arquivos .md manualmente (SEM unstructured)
for path in Path(DOCS_PATH).rglob("*.md"):
    try:
        loader = TextLoader(str(path), encoding="utf-8")
        docs = loader.load()

        # 🔗 salva origem (importante para links no chat)
        for doc in docs:
            doc.metadata["source"] = str(path)

        documents.extend(docs)

    except Exception as e:
        print(f"⚠️ Erro ao carregar {path}: {e}")

print(f"📄 {len(documents)} documentos carregados")

# ❗ validação
if len(documents) == 0:
    print("❌ Nenhum documento encontrado em docs/")
    exit(1)

# ✂️ dividir em chunks
splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

print(f"✂️ {len(docs)} chunks criados")

# 🧠 embeddings
print("🧠 Gerando embeddings...")

if not os.getenv("OPENAI_API_KEY"):
    print("❌ OPENAI_API_KEY não encontrada!")
    exit(1)

embeddings = OpenAIEmbeddings()

# 🗑️ remove DB antigo (evita conflito)
if os.path.exists(DB_PATH):
    import shutil
    shutil.rmtree(DB_PATH)
    print("🗑️ DB antigo removido")

# 💾 cria banco vetorial
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory=DB_PATH
)

db.persist()

print("✅ Banco vetorial criado com sucesso em:", DB_PATH)
