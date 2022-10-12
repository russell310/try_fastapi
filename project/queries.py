import strawberry
from apps.user.queries import UserQuery


@strawberry.type
class Query(
    UserQuery
):
    pass
