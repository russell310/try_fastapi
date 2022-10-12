from typing import List

from fastapi import HTTPException
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError

from . import users_router
from .models import UserSchema, User, UserInSchema


class Status(BaseModel):
    message: str


@users_router.get("/", response_model=List[UserSchema])
async def users(search: str = None):
    if search:
        return await UserSchema.from_queryset(User.filter(username__icontains=search))
    return await UserSchema.from_queryset(User.all())


@users_router.post("/create/", response_model=UserSchema)
async def create_user(user: UserInSchema):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await UserSchema.from_tortoise_orm(user_obj)


@users_router.get("/{user_id}/", response_model=UserSchema, responses={404: {"model": HTTPNotFoundError}})
async def get_user(user_id: int):
    return await UserSchema.from_queryset_single(User.get(id=user_id))


@users_router.put("/{user_id}/", response_model=UserSchema, responses={404: {"model": HTTPNotFoundError}})
async def update_user(user_id: int, user: UserInSchema):
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await UserSchema.from_queryset_single(User.get(id=user_id))


@users_router.delete("/{user_id}/", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
