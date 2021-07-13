from sqlalchemy.orm import Session

from app.infra.repository.base_repository import BaseRepository
from app.infra.sql_app.models import User


class UserRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
        self._db = db

    def get_user(self, user_id: int):
        return self._db.query(User).filter(User.id == user_id)
