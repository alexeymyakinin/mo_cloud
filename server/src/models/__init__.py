from sqlalchemy import Column, BigInteger, TIMESTAMP, func, MetaData
from sqlalchemy.orm import as_declarative

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)


@as_declarative(metadata=metadata)
class Base:
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    created_at = Column(TIMESTAMP, nullable=False, default=func.utcnow())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.utcnow(), onupdate=func.utcnow())
    deleted_at = Column(TIMESTAMP, nullable=True, default=func.utcnow())
