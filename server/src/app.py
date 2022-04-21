from fastapi import FastAPI

from server.src.routes.service import service_router
from server.src.routes.user import user_router


def add_middlewares(app: FastAPI):
    pass


def add_routes(app: FastAPI):
    app.include_router(user_router)
    app.include_router(service_router)


def build_app() -> FastAPI:
    app = FastAPI()
    add_routes(app)
    add_middlewares(app)
    return app

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('server.src.app:build_app', reload=True, factory=True)