import pytest as pytest

from server.src.dependencies.repository import RepositoryMap
from server.src.models.service import Service
from server.src.models.user import User
from server.src.schemas.service import ServiceSchemaDB
from server.src.schemas.user import UserSchemaDB


@pytest.mark.parametrize(("model", "schema", "db"), [(User, UserSchemaDB, ...), (Service, ServiceSchemaDB, ...)])
def test_get_repository(model, schema, db):
    repo = RepositoryMap.get(model, schema)(db)
    assert repo.model == model
    assert repo.schema == schema
