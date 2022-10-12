import strawberry

from .scalars import User, UserExists, UserDeleted, UserNotFound

AddUserResponse = strawberry.union("AddUserResponse", (User, UserExists))
UpdateUserResponse = strawberry.union("UpdateUserResponse", (User, UserNotFound))
DeleteUserResponse = strawberry.union("DeleteUserResponse", (UserDeleted, UserNotFound))
