from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    @property
    def connection(self) -> Session:
        return self._db
