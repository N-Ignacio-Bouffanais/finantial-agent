from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import os

def initialize_vector_store(documents):
    embeddings = OllamaEmbeddings(model="deepseek-r1:14b")
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    return vector_store