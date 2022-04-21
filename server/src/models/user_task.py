from sqlalchemy import Column, BigInteger, ForeignKey, Enum
from sqlalchemy.orm import relationship

from server.src.models import Base
from server.src.models.task import Task
from server.src.models.user import User
from server.src.shared.types import UserTaskType


class UserTask(Base):
    __tablename__ = "user_task"

    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False, index=True)
    task_id = Column(BigInteger, ForeignKey("task.id"), nullable=False, index=True)
    user_type = Column(Enum(UserTaskType), nullable=False, index=True)

    user = relationship(User)
    task = relationship(Task)
