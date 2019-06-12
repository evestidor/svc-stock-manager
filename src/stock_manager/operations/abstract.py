from abc import ABC, abstractmethod


class AbstractOperation(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
