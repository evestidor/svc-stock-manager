from abc import ABC, abstractmethod

from .domain import (
    Account,
    Portfolio,
)


class PortfolioStorage(ABC):

    @property
    @abstractmethod
    def DoesNotExist(self) -> Exception:
        pass

    @abstractmethod
    def create(self, portfolio: Portfolio) -> Portfolio:
        pass

    @abstractmethod
    def get_by_account(self, account: Account) -> Portfolio:
        pass
