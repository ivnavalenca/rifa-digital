
# ingest.py
#
# This script indexes the project documentation to build a vector database
# used by the Engineering Copilot (RAG system).
#
# It reads all Markdown files inside the docs/ directory and creates
# embeddings that allow semantic search over the engineering documentation.
#
# Output directory:
# copilot/db/

import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

DOCS_PATH = "docs"
DB_PATH = "copilot/db"

def main():

    print("Loading documentation...")

    loader = DirectoryLoader(DOCS_PATH, glob="**/*.md")
    documents = loader.load()

    print("Splitting documents...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    docs = splitter.split_documents(documents)

    print("Creating embeddings...")

    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=DB_PATH
    )

    db.persist()

    print("Knowledge base created at:", DB_PATH)


if __name__ == "__main__":
    main()
