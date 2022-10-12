import strawberry
from pydantic import typing
from apps.user.resolvers import get_users
from apps.user.scalars import User as UserScalars


@strawberry.type
class UserQuery:
    @strawberry.field
    async def users(self, username: typing.Optional[str] = None) -> typing.List[UserScalars]:
        users_data_list = await get_users(username)
        return users_data_list
