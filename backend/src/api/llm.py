from fastapi import APIRouter


router = APIRouter()

@router.post('/ask', tags=["llm"])

async def ask_question(question: str):
  return {"response": "Esto es lo que yo puedo responder acerca de:" + question}
