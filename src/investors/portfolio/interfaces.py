from abc import ABC, abstractmethod

from .domain import Portfolio


class PortfolioStorage(ABC):

    @property
    @abstractmethod
    def DoesNotExist(self) -> Exception:
        pass

    @abstractmethod
    def create(self, portfolio: Portfolio) -> Portfolio:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Portfolio:
        pass
