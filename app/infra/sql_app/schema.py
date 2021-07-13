from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int
    name: str
    email: str
    password: str
    role_id: int

    class Config:
        orm_mode = True
