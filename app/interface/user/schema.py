from typing import Optional

from pydantic import BaseModel, Field, validator

from app.infra.sql_app.db import db
from app.infra.sql_app.models import RoleModel


class UserBase(BaseModel):
    name: str = Field(max_length=20)
    email: str = Field(max_length=30)
    role_id: int


class UserCreate(UserBase):
    password: Optional[str] = Field(max_length=16)

    @validator('role_id')
    def role_id_exists(cls, v):
        role = db.query(RoleModel).filter_by(id=v).first()
        assert role, "role_id doesn't exists"
        return v


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
