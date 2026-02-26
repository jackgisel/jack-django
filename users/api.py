import msgspec
from django_bolt import BoltAPI

from users.models import User

api = BoltAPI()


class UserSchema(msgspec.Struct):
    id: int
    username: str
    email: str
    is_active: bool


class UserListSchema(msgspec.Struct):
    count: int
    users: list[UserSchema]


@api.get("/users")
async def list_users() -> UserListSchema:
    users = []
    async for user in User.objects.filter(is_active=True):
        users.append(
            UserSchema(
                id=user.id,
                username=user.username,
                email=user.email,
                is_active=user.is_active,
            )
        )
    return UserListSchema(count=len(users), users=users)


@api.get("/users/{user_id}")
async def get_user(user_id: int) -> UserSchema:
    user = await User.objects.aget(id=user_id)
    return UserSchema(
        id=user.id,
        username=user.username,
        email=user.email,
        is_active=user.is_active,
    )
