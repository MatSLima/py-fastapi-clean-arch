from abc import ABCMeta


class User(metaclass=ABCMeta):
    id: int
    name: str
    email: str
    role_id: int
    password: str
