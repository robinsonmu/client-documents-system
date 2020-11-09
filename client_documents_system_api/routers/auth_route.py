from fastapi import APIRouter, HTTPException, Depends, status
from config.app_security import JwtManager
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user_schemas import UserBase
from config.app_security import Token
from datetime import datetime, timedelta
from config.app_config import settings
from db.database import SessionLocal
from models import users_models


router = APIRouter()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


jwt_manager = JwtManager(settings.access_token_expire_minutes,
                         settings.secret_key,
                         settings.algorithm)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = jwt_manager.authenticate_user(get_db(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = jwt_manager.create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
