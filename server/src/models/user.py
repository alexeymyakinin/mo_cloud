from sqlalchemy import Column, String, BigInteger

from server.src.models import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    phone = Column(String(255), nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
