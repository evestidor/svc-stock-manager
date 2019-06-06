from abc import ABC, abstractmethod

from ..exceptions import PortfolioDoesNotExist
from ..domain import Portfolio


class PortfolioStorage(ABC):
    DoesNotExist = PortfolioDoesNotExist

    @abstractmethod
    def create(self, portfolio: Portfolio) -> Portfolio:
        pass

    @abstractmethod
    def get_by_account_id(self, account_id: int) -> Portfolio:
        pass
