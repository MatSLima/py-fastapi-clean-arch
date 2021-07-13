from abc import ABCMeta, abstractmethod

from app.domain.interfaces import IBaseRepository


class BaseUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, repo: IBaseRepository, **kwargs):
        raise NotImplementedError(self.__class__.__name__)
