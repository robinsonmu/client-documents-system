from sqlalchemy.orm import Session
from models import users_models
from schemas import user_schemas
from config import app_security


def get_user(db: Session, user_id: int):
    return db.query(users_models.User).filter(users_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    results = db.query(users_models.User).filter(users_models.User.email == email)
    user = results.first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    security_utils = app_security.JwtManager()
    hashed_password = security_utils.get_password_hash(user.password)
    db_user = users_models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
