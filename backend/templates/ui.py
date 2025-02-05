import streamlit as st

def show_header():
    st.markdown("""
    # Bienvenido a RAG Assistant 🤖
    ### Sube tu PDF y haz preguntas sobre su contenido
    ---
    """)

def show_sidebar():
    with st.sidebar:
        st.markdown("""
        **Características:**
        - Procesamiento de documentos PDF
        - Búsqueda semántica con DeepSeek
        - Almacenamiento vectorial con ChromaDB

        ***Pronto:***
        - Busqueda mediante APIS externas
        - transformacion de texto a Queries SQL
        """)