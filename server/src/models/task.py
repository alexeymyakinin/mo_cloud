from sqlalchemy import Column, String, BigInteger

from server.src.models import Base, TimestampMixin


class Task(Base, TimestampMixin):
    __tablename__ = "task"

    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String)
