from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from server.src.models import Base
from server.src.models.user import User


class Service(Base):
    __tablename__ = "service"

    name = Column(String(255), nullable=False)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False, index=True)

    user = relationship(User)
