from fastapi import FastAPI

from app.infra.sql_app import models
from app.infra.sql_app.db import Base, engine


async def connect_to_db() -> None:
    models.Base.metadata.create_all(bind=engine)
    return Base


async def close_db_connection(app: FastAPI) -> None:
    await app.state.pool.close()
