from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from server.src.dependencies.repository.task import TaskRepository

router = InferringRouter()


@cbv(router)
class TaskCBV:
    repository: TaskRepository = Depends()

    @router.get("/api/task/{task_id}")
    async def get_task(self, task_id: int):
        pass

    @router.get("/api/task")
    async def search_task(self):
        pass

    @router.post("/api/task")
    async def create_task(self):
        pass

    @router.patch("/api/task")
    async def update_task(self):
        pass
