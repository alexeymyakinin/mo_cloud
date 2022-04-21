from __future__ import annotations

import functools
from typing import TypeVar, Type, Callable

from fastapi import Depends
from sqlalchemy import insert, select

from server.src.models import Base
from server.src.schemas import Schema

T = TypeVar("T", bound=Base)
V = TypeVar("V", bound=Schema)


def get_database():
    return 1


class Repository:
    def __init__(self, model: Type[T], schema: Type[V], database: get_database = Depends()):
        self._model = model
        self._schema = schema
        self._database = database

    @property
    def model(self):
        return self._model

    @property
    def schema(self):
        return self._schema

    def _get_create_query(self, value: V):
        return insert(self._model).values(**value.dict()).returning(self._model)

    def _get_select_query(self, where: dict, limit: int = 100, offset: int = 0):
        return select(self._model).where(**where).limit(limit).offset(offset)


class RepositoryMap:
    store = dict()

    @classmethod
    def get(cls, model, schema) -> Callable[..., Repository]:
        return functools.partial(cls.store.get(model, Repository), model, schema)

    @classmethod
    def set(cls, model, repo):
        cls.store[model] = repo
