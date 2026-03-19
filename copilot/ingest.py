from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

print("📥 Indexando documentos...")

loader = DirectoryLoader("docs", glob="**/*.md")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

db = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(),
    persist_directory="db"
)

db.persist()

print("✅ Base vetorial criada!")
