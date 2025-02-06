from fastapi import FastAPI
from api import auth, llm
from config import settings
import uvicorn

app = FastAPI(title="Finantial Api Agent", description="This is an API for LLM langchain project")


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(llm.router, prefix="/ask", tags=["llm"])


if __name__ == "__main__":
    print(f"El servidor está corriendo en http://{settings.host}:{settings.port}")
    uvicorn.run(app, host=settings.host, port=settings.port, reload=True)
