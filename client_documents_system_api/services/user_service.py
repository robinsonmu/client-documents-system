from sqlalchemy.orm import Session
from models import users_models
from schemas import user_schemas


def get_user(db: Session, user_id: int):
    return db.query(users_models.User).filter(users_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    results = db.query(users_models.User).filter(users_models.User.email == email)
    user = results.first()
    print(f"Session db {db} {email} \n R> {results}")
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = users_models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
