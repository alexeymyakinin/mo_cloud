from fastapi import FastAPI

from server.src.dependencies import database
from server.src.routes.task import router
from server.src.routes.user import router


async def on_startup():
    await database.connect()


async def on_shutdown():
    await database.disconnect()


def add_events(app: FastAPI):
    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)


def add_middlewares(app: FastAPI):
    pass


def add_routes(app: FastAPI):
    app.include_router(router)
    app.include_router(router)


def build_app() -> FastAPI:
    app = FastAPI()
    add_events(app)
    add_routes(app)
    add_middlewares(app)
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server.src.app:build_app", reload=True, factory=True)
