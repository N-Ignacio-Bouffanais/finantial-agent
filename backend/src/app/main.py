from fastapi import FastAPI
from src.config.settings import settings
from src.api import auth, llm
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Finantial Api Agent", description="This is an API for LLM langchain project")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT"],  
    allow_headers=["*"],  # Permite todos los headers
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(llm.router, prefix="/chat", tags=["llm"])


if __name__ == "__main__":
    print(f"El servidor está corriendo en http://{settings.host}:{settings.port}")
    uvicorn.run(app, host=settings.host, port=settings.port, reload=True)
