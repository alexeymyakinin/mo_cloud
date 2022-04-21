from __future__ import annotations

from abc import abstractmethod, ABC
from typing import TypeVar

from databases.core import Connection
from fastapi import Depends
from sqlalchemy import insert, select

from server.src.dependencies import get_connection
from server.src.models import Base
from server.src.schemas import Schema

T = TypeVar("T", bound=Base)
V = TypeVar("V", bound=Schema)


class RepositoryABC(ABC):
    def __init__(self, database: Connection = Depends(get_connection)):
        self._database = database

    @property
    @abstractmethod
    def model(self):
        raise NotImplementedError()

    def _get_create_query(self, value: V):
        return insert(self.model).values(**value.dict()).returning(self.model)

    def _get_select_query(self, where: dict, limit: int = 100, offset: int = 0):
        return select(self.model).where(**where).limit(limit).offset(offset)
