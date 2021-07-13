from fastapi import APIRouter

from app.interface.user import router as users

router = APIRouter()
router.include_router(users.router, tags=["users"])
