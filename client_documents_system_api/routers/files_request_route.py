from schemas import files_request_schemas, mail_schemas
from schemas.user_schemas import User
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session
from services import user_service, files_request_service
from mail import mail_sender


router = APIRouter()
mailer = mail_sender.MailSender()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=files_request_schemas.FilesRequest)
async def create_request(files_request: files_request_schemas.FilesRequest, db: Session = Depends(get_db)):
    stored_request = files_request_service.create_files_request(db, files_request)
    print(f"{files_request}")
    client = user_service.get_user(db, files_request.client_id)
    email_info = mail_schemas.RequestCreated(client_email=client.email, subject="Peticion de archivos")

    await mailer.send_confirmation_to_client(email_info)

    return stored_request


@router.get("/", response_model=List[files_request_schemas.FilesRequest])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    requests = files_request_service.get_requests(db, skip=skip, limit=limit)
    return requests
