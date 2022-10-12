from apps.user.models import User
from apps.user.scalars import User as UserScalars, UserDeleted, UserNotFound, UserExists
from helpers.helper import get_valid_data


async def get_users(name):
    if name:
        users = await User.filter(username__icontains=name)
    else:
        users = await User.all()
    users_data_list = []
    for user in users:
        data = get_valid_data(user, User)
        users_data_list.append(UserScalars(**data))

    return users_data_list


async def add_user(*args, **kwargs):
    username = kwargs.get('username')
    check = await User.filter(username=username)
    if check:
        return UserExists()
    user = await User.create(**kwargs)
    data = get_valid_data(user, User)
    return UserScalars(**data)


async def update_user(user_id, **kwargs):
    try:
        user = await User.get(id=user_id)
    except:
        return UserNotFound()
    await User.filter(id=user_id).update(**kwargs)
    user = await user.get(id=user_id)
    data = get_valid_data(user, User)
    return UserScalars(**data)


async def delete_user(user_id):
    count = await User.filter(id=user_id).delete()
    if count == 0:
        return UserNotFound()
    return UserDeleted()
