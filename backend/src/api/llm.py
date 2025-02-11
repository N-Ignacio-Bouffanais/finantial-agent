from fastapi import APIRouter, Body
from src.schemas.schema import ChatRequest

router = APIRouter()


@router.post("/", tags=["llm"])
async def chat_endpoint(
    request: ChatRequest = Body(...),
):
    return {"message": f"Recibido: {request.question}"}
