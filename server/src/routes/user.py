from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from server.src.dependencies.repository.user import UserRepository

router = APIRouter()


@cbv(router)
class UserCBV:
    repo: UserRepository = Depends()

    @router.get("/api/user/{username}")
    async def get_user(self, username: str):
        pass

    @router.get("/api/user")
    async def search_user(self):
        pass

    @router.post("/api/user")
    async def create_user(self):
        pass

    @router.patch("/api/user")
    async def update_user(self):
        pass
