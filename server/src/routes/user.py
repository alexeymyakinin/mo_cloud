import asyncio
import json

from fastapi import APIRouter, Depends

from server.src.dependencies import Repository
from server.src.dependencies.container import docker_client
from server.src.models.user import User
from server.src.schemas.user import UserSchemaDB

user_router = APIRouter()


@user_router.get("/api/user")
async def get_user(repo: Repository = Depends(Repository(User, UserSchemaDB))):
    return repo.schema


@user_router.post("/api/user")
async def create_user():
    pass


@user_router.patch("/api/user")
async def update_user():
    pass


@user_router.get("/api/user/images")
async def list_user_images():
    return docker_client.images.list()


@user_router.get("/api/user/images/{image_id}")
async def get_user_image():
    pass


@user_router.get("/api/user/containers")
async def list_user_containers():
    ctrs = await asyncio.to_thread(docker_client.containers.list)
    return json.dumps(ctrs, default=str)


@user_router.get("/api/user/containers/{container_id}")
async def get_user_container():
    pass
