from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings


def initialize_vector_store(documents):
    embeddings = OllamaEmbeddings(model="deepseek-r1:8b")

    vector_store = Chroma(
        collection_name="document_vectors",
        embedding_function=embeddings,
        persist_directory="./chroma_db",
    )

    if documents:
        vector_store.add_documents(documents)

    return vector_store
