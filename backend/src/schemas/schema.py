from pydantic import BaseModel, EmailStr, validator
import re


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError(
                "La contraseña debe contener al menos un carácter especial."
            )
        return value


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class ChatRequest(BaseModel):
    question: str
    # user_id: int


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
