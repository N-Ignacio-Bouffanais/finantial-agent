from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    financial_api_key: str = Field(..., env="FINANCIAL_API_KEY")
    ollama_model: str = Field("deepseek-r1:14b", env="OLLAMA_MODEL")
    ollama_endpoint: str = Field("http://localhost:11434", env="OLLAMA_ENDPOINT")
    max_pdf_pages: int = Field(50, env="MAX_PDF_PAGES")

    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        extra = "allow"

settings = Settings()
