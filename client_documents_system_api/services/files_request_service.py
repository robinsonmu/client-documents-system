from sqlalchemy.orm import Session
from models import file_requests_models
from schemas import files_request_schemas
from common import enums


def create_files_request(db: Session, files_request: files_request_schemas.FilesRequest):
    db_request = file_requests_models.FilesRequest(client_id=files_request.client_id,
                                                   state=enums.FilesRequestStatus.not_reviewed,
                                                   description=files_request.description)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def get_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(file_requests_models.FilesRequest).offset(skip).limit(limit).all()
