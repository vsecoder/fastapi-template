from fastapi import APIRouter

from app.db.functions import User

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = await User.get_dict(user_id=user_id)
    return user
