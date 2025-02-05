from fastapi import FastAPI
from app.api import auth, llm
from app.config import settings

app = FastAPI(title="Finantial Api Agent", description="This is an API for LLM langchain project")


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(llm.router, prefix="/ask", tags=["llm"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)