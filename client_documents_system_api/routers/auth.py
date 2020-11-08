from fastapi import APIRouter, HTTPException, Depends
from config.app_security import JwtManager
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import UserBase
from config.app_security import Token
from datetime import datetime, timedelta
from config.app_config import settings
router = APIRouter()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

jwt_manager = JwtManager(settings.access_token_expire_minutes,
                         settings.secret_key,
                         settings.algorithm)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = jwt_manager.authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = jwt_manager.create_access_token(
        data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
