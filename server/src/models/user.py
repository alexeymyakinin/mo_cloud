from sqlalchemy import Column, String

from server.src.models import Base


class User(Base):
    __tablename__ = "user"

    username = Column(String(255), nullable=False, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    phone = Column(String(255), nullable=False, unique=True, index=True)
