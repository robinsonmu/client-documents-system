from fastapi import APIRouter, HTTPException, Depends
from schemas.user import User
router = APIRouter()


@router.post("/", response_model=User)
async def store_user(form_data: OAuth2PasswordRequestForm = Depends()):
    print("Saving")
