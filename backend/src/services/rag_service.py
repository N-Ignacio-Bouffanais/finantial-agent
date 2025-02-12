from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from typing import List


def answer_question(question: str, documents: List):
    model = OllamaLLM(model="deepseek-r1:14b")

    template = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know. Answer always in Spanish and be concise.

    Contexto: {context}
    Pregunta: {question}

    Respuesta:
    """

    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    return chain.invoke({"question": question, "context": context})
