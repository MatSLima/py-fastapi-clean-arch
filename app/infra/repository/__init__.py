from typing import Type, Callable

from fastapi import Depends
from sqlalchemy.orm import Session

from app.infra.repository.base_repository import BaseRepository
from app.infra.sql_app.db import get_db


def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[Session], BaseRepository]:
    def _get_repo(
        db: Session = Depends(get_db),
    ) -> BaseRepository:
        return repo_type(db)

    return _get_repo
