import strawberry

from apps.user.fragments import AddUserResponse, DeleteUserResponse, UpdateUserResponse
from apps.user.resolvers import add_user, delete_user, update_user


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_user(self, username: str, name: str, email: str) -> AddUserResponse:
        add_user_resp = await add_user(username=username, name=name, email=email)
        return add_user_resp

    @strawberry.mutation
    async def update_user(self, user_id: int, username: str, name: str, email: str) -> UpdateUserResponse:
        add_user_resp = await update_user(user_id, username=username, name=name, email=email)
        return add_user_resp

    @strawberry.mutation
    async def delete_user(self, user_id: int) -> DeleteUserResponse:
        delete_user_resp = await delete_user(user_id)
        return delete_user_resp
