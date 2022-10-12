from pydantic import typing

import strawberry


@strawberry.type
class User:
    id: int
    username: typing.Optional[str] = ""
    email: typing.Optional[str] = ""
    name: typing.Optional[str] = ""


@strawberry.type
class UserExists:
    message: str = "User with this username already exists"


@strawberry.type
class UserNotFound:
    message: str = "Couldn't find useruser with the name"


@strawberry.type
class UserDeleted:
    message: str = "User deleted"
