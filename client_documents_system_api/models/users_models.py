from db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_employee = Column(Boolean, default=False)

    client_data = relationship("Client", uselist=False, back_populates="user_data")


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, index=True)

    address = Column(String, nullable=False)
    occupation = Column(String, default=None)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user_data = relationship("User", uselist=False, back_populates="client_data")
    files_requests = relationship("FilesRequest", back_populates="client")
