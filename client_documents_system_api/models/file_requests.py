from db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from common import enums
from sqlalchemy.orm import relationship


class FilesRequest(Base):
    __tablename__ = "files_request"

    id = Column(Integer, primary_key=True, index=True)
    state = Column("state", Enum(enums.FilesRequestStatus, nullable=False))
    comments = Column("comments", String(1000), nullable=False)

    required_documents = relationship("RequiredDocument", back_populates="owner_request")


class RequiredDocument(Base):
    __tablename__ = "required_document"

    id = Column(Integer, primary_key=True, index=True)

    path = Column("path", String(500), nullable=False)
    name = Column("name", String(200), nullable=False)
    description = Column("description", String(1000), nullable=False)
    status = Column("status", Enum(enums.FilesRequestStatus), nullable=False)

    files_request_id = Column("FilesRequest", ForeignKey("files_request.id"))
    owner_request = relationship("FilesRequest", back_populates="required_documents")
