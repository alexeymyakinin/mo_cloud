from server.src.dependencies.repository import RepositoryABC
from server.src.models.task import Task


class TaskRepository(RepositoryABC):
    @property
    def model(self):
        return Task
