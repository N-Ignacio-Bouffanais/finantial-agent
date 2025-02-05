from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import os

def initialize_vector_store(documents):
    # Inicializar el modelo de embeddings
    embeddings = OllamaEmbeddings(model='deepseek-r1:8b')
    
    # Crear o conectar a la base de datos ChromaDB
    vector_store = Chroma(collection_name="document_vectors", embedding_function=embeddings, persist_directory="./chroma_db")

    # Agregar los documentos al vector store
    vector_store.add_documents(documents)
    
    return vector_store