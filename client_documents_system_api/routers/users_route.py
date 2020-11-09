from typing import List
from fastapi import APIRouter, HTTPException, Depends
from schemas.user_schemas import User
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session
from services import user_service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users
