from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from schemas.user import User, UserInDB


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class JwtManager:
    def __init__(self, token_expiry_minutes: int, secret_key: str, algorithm: str):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
        self.token_expiry_minutes = token_expiry_minutes
        self.secret_key = secret_key
        self.algorithm = algorithm

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def get_user(self, db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)

    def authenticate_user(self, db, username: str, password: str):
        user = self.get_user(db, username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(self, data: dict):
        expires_delta = timedelta(minutes=self.token_expiry_minutes)
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def oauth2_scheme(self):
        return self.oauth2_scheme

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(self, current_user: User = Depends(get_current_user)):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
