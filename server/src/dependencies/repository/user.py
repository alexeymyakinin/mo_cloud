from server.src.dependencies.repository import RepositoryABC
from server.src.models.user import User


class UserRepository(RepositoryABC):
    @property
    def model(self):
        return User
