from fastapi import APIRouter


router = APIRouter()

@router.get("/auth", tags=["authentication"])

async def login():
  pass


async def register():
  pass
  