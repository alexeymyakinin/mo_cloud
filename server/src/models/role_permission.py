from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship

from server.src.models import Base
from server.src.models.permission import Permission
from server.src.models.role import Role


class RolePermission(Base):
    __tablename__ = "role_permission"

    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    role = relationship(Role)
    role_id = Column(BigInteger, ForeignKey("role.id"), nullable=False, index=True)
    permission = relationship(Permission)
    permission_id = Column(BigInteger, ForeignKey("permission.id"), nullable=False, index=True)
