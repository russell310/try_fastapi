import strawberry
from apps.user.mutations import UserMutation


@strawberry.type
class Mutation(
    UserMutation
):
    pass
