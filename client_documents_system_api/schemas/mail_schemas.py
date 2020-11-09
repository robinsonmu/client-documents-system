from typing import List, Optional
from pydantic import BaseModel, EmailStr


class RequestCreated(BaseModel):
    client_email: EmailStr
    subject: str
