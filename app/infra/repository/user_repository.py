from typing import List

from app.domain.interfaces import IUserRepository
from app.infra.sql_app import models
from app.infra.sql_app.models import UserModel
from app.interface.user import schema


class UserRepository(IUserRepository):
    def create_user(self, user: schema.UserCreate) -> UserModel:
        db_item = models.UserModel(**user.dict())
        self._db.add(db_item)
        self._db.commit()
        self._db.refresh(db_item)
        return db_item

    def get_users(self, query_param=None) -> List[UserModel]:
        return self._db.query(UserModel).filter_by(**query_param).all()
