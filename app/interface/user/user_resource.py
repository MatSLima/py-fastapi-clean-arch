from typing import List

from fastapi import APIRouter, Depends, Body
from starlette import status

from app.infra.repository import get_repository
from app.infra.repository.user_repository import UserRepository
from app.interface.user import schema
from app.usecases.user_usecase import get_user_use_case, create_user_use_case

router = APIRouter()


@router.get("/", response_model=List[schema.UserRead], name="user:list-users")
async def list_users(
        role_id: int = None,
        user_repo: UserRepository = Depends(get_repository(UserRepository))
) -> List[schema.UserRead]:
    users = get_user_use_case.execute(user_repo, role_id=role_id)
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.UserRead, name="user:create-user")
async def create_user(
    user: schema.UserCreate = Body(..., embed=True, alias="user"),
    user_repo: UserRepository = Depends(get_repository(UserRepository))
) -> schema.UserRead:
    user = create_user_use_case.execute(user_repo, user=user)
    return user
