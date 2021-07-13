from typing import Type, Callable

from fastapi import Depends
from sqlalchemy.orm import Session

from app.domain.interfaces import IBaseRepository
from app.infra.repository.base_repository import BaseRepository
from app.infra.sql_app.db import get_db


def get_repository(
    repo_type: Type[IBaseRepository],
) -> Callable[[Session], IBaseRepository]:
    def _get_repo(
        db: Session = Depends(get_db),
    ) -> IBaseRepository:
        return repo_type(db)

    return _get_repo
