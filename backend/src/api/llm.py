from fastapi import APIRouter, Body, File, HTTPException
from src.services.pdf_processor import process_pdf
from src.services.rag_service import answer_question
from src.services.vector_store import initialize_vector_store
from src.schemas.schema import ChatRequest, QuestionRequest, AnswerResponse
from fastapi import UploadFile

router = APIRouter()


@router.post("/", tags=["llm"])
async def chat_endpoint(
    request: ChatRequest = Body(...),
):
    return {"message": f"Recibido: {request.question}"}


@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        chunks = process_pdf(file)
        vector_store = initialize_vector_store(chunks)
        return {"message": "PDF procesado exitosamente", "chunks": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ask/", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        vector_store = initialize_vector_store(
            []
        )  # Se debe cargar los documentos previamente
        related_documents = vector_store.similarity_search(request.question, k=3)
        answer = answer_question(request.question, related_documents)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
