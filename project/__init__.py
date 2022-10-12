from fastapi import FastAPI
from apps.user import users_router
from project.database import init_db


def create_app() -> FastAPI:
    app = FastAPI()

    @app.on_event("startup")
    async def startup_event():
        init_db(app)

    app.include_router(users_router, prefix="/api")

    return app
