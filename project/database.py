import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .config import settings

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["apps.user.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["apps.user.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
