from fastapi import APIRouter
from app.handlers.user.api import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/user", tags=["user"])

@router.get("/")
async def api_root():
    return {"ping": "pong"}
