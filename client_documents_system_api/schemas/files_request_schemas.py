from typing import List, Optional
from pydantic import BaseModel
from common import enums


class FilesRequest(BaseModel):
    client_id: int
    state: Optional[enums.FilesRequestStatus] = enums.FilesRequestStatus.reviewed
    comments: Optional[str] = None
    description: str

    class Config:
        orm_mode = True


class RequiredDocument(BaseModel):
    path: str
    name: str
    description: str
    status: enums.FilesRequestStatus = enums.FilesRequestStatus.not_reviewed
    files_request_id: int

    class Config:
        orm_mode = True
