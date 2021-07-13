from sqlalchemy.orm import Session

from app.domain.interfaces import IBaseRepository


class BaseRepository(IBaseRepository):
    @property
    def connection(self) -> Session:
        return self._db
