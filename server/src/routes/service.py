from fastapi import APIRouter

service_router = APIRouter()


@service_router.get("/api/service")
async def get_services():
    pass


@service_router.post("/api/service/images")
async def get_images():
    pass
