from fastapi import APIRouter


router = APIRouter()

@router.get("/login", tags=["authentication"])
async def login():
  pass


@router.get("/register", tags=["authentication"])
async def register():
  pass
  