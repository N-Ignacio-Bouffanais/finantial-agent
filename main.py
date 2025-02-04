import streamlit as st
from modules.document_processor import process_pdf
from modules.vector_store import initialize_vector_store
from templates.styles import load_css
from templates.ui import show_header, show_sidebar
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def answer_question(question, documents):
    model = OllamaLLM(model='deepseek-r1:14b')
    
    template = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Answer always in Spanish and be consice.
    Contexto: {context}
    
    Pregunta: {question}
    
    Respuesta:"""
    
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    
    return chain.invoke({"question": question, "context": context})

def main():
    load_css()
    show_header()
    show_sidebar()

    pdf_file = st.file_uploader("Sube tu PDF", type=["pdf"])
    
    if pdf_file is not None:
        chunks = process_pdf(pdf_file)
        vector_store = initialize_vector_store(chunks)
        
        question = st.text_input("Hola, adelante preguntame lo que quieras:")
        if question:
            st.chat_message("user").write(question)
            related_documents = vector_store.similarity_search(question, k=3)
            answer = answer_question(question, related_documents)
            st.chat_message("assistant").write(answer)
            

if __name__ == "__main__":
    main()