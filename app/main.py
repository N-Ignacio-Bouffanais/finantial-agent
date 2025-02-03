import streamlit as st
from modules.document_processor import process_pdf
from modules.vector_store import initialize_vector_store
from templates.styles import load_css
from templates.ui import show_header, show_sidebar

def main():
    # Configuración inicial
    load_css()
    show_header()
    show_sidebar()
    
    # Carga de documentos
    pdf_file = st.file_uploader("Sube tu PDF", type=["pdf"])
    
    if pdf_file is not None:
        # Procesamiento del documento
        chunks = process_pdf(pdf_file)
        
        # Inicialización del vector store
        retriever = initialize_vector_store(chunks)
        
        # Interfaz de consulta
        query = st.text_input("Haz tu pregunta:")
        if query:
            # Aquí irá la lógica de búsqueda y respuesta
            pass

if __name__ == "__main__":
    main()