import streamlit as st
from modules.document_processor import process_pdf
from modules.vector_store import initialize_vector_store
from templates.styles import load_css
from templates.ui import show_header, show_sidebar

def answer_question(question, documents):
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
        vector_store.add_documents(chunks)

        question = st.text_input("Hola, adelante preguntame lo que quieras:")
        if question:
             st.chat_message("user").write(question)
             related_documents = vector_store.similarity_search(question)
             answer = answer_question(question, related_documents)
             st.chat_message("assistant").write(answer)
            

if __name__ == "__main__":
    main()