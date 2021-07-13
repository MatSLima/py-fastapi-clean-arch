from fastapi import APIRouter

from app.interface.routes.user import user_resource

router = APIRouter()
router.include_router(user_resource.router, prefix="/user")
