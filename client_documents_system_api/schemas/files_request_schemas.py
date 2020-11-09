from typing import List, Optional
from pydantic import BaseModel
from common import enums


class RequiredDocument(BaseModel):
    name: str
    description: str
    state: enums.FilesRequestStatus = enums.FilesRequestStatus.not_reviewed
    path: Optional[str] = None

    files_request_id: Optional[int] = None

    class Config:
        orm_mode = True

class FilesRequest(BaseModel):
    client_id: int
    state: Optional[enums.FilesRequestStatus] = enums.FilesRequestStatus.reviewed
    comments: Optional[str] = None
    description: str

    required_documents: List[RequiredDocument] = []

    class Config:
        orm_mode = True

