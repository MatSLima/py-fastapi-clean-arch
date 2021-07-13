import random
import string
from typing import List

from app.domain.entities import User
from app.domain.interfaces import IUserRepository
from app.usecases.base_usecase import BaseUseCase


class GetUserUseCase(BaseUseCase):
    def execute(self, user_repo: IUserRepository, **kwargs) -> List[User]:
        params = self.remove_empty_params(kwargs)
        return user_repo.get_users(query_param=params)

    @staticmethod
    def remove_empty_params(dictionary):
        return {k: v for k, v in dictionary.items() if v is not None}


class CreateUserUseCase(BaseUseCase):
    def execute(self, user_repo: IUserRepository, **kwargs) -> User:
        user = kwargs.get('user', None)
        if not user.password:
            user.password = self.generate_random_password()

        return user_repo.create_user(user)

    @staticmethod
    def generate_random_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(16))


get_user_use_case = GetUserUseCase()
create_user_use_case = CreateUserUseCase()
