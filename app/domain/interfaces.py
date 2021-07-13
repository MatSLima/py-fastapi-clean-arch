from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.entities import User


class IBaseRepository(metaclass=ABCMeta):
    def __init__(self, db) -> None:
        self._db = db


class IUserRepository(IBaseRepository):
    @abstractmethod
    def get_users(self, query_param: dict = None) -> List[User]:
        raise NotImplementedError(self.__class__.__name__)

    @abstractmethod
    def create_user(self, user: User) -> User:
        raise NotImplementedError(self.__class__.__name__)
