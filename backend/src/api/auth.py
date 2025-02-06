from fastapi import APIRouter
from schemas.user import UserCreate


router = APIRouter()

@router.post("/login", tags=["authentication"])
async def login():
  pass


@router.post("/register", tags=["authentication"])
async def register(user: UserCreate):
  return user.email
    


@router.post("/newpass", tags=["authentication"])
async def newpass():
  pass
