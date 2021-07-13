from fastapi import APIRouter

from app.interface.routes.user import api as users

router = APIRouter()
router.include_router(users.router, tags=["users"])
