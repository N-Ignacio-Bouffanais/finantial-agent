from fastapi import APIRouter


router = APIRouter()

@router.post("/login", tags=["authentication"])
async def login():
  pass


@router.post("/register", tags=["authentication"])
async def register():
  #Buscar el usuario si existe en la base de datos
  pass
  
@router.post("/newpass", tags=["authentication"])
async def newpass():
  pass
  