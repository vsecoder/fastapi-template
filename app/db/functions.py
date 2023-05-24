from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


class User(models.User):
    """
    User model, contains all methods for working with users.
    """
    @classmethod
    async def get_dict(cls, user_id: int) -> Union[dict, None]:
        """
        Get user by id.
        :param user_id: User id.
        :return: User dict.
        """
        try:
            return await cls.get(id=user_id)
        except DoesNotExist:
            return None
