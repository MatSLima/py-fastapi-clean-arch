from fastapi import APIRouter, Depends

from app.infra.repository import get_repository
from app.infra.repository.user_repository import UserRepository
from app.infra.sql_app import schema

router = APIRouter()


@router.get("/{user_id}", response_model=schema.User, name="user:get-user")
async def retrieve_article_by_slug(
        user_id: int,
        user_repo: UserRepository = Depends(get_repository(UserRepository))
) -> schema.User:
    return user_repo.get_user(user_id)
