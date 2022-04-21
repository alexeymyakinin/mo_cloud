from sqlalchemy import Column, BigInteger, String

from server.src.models import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
