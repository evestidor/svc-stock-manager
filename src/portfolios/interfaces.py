from abc import ABC, abstractmethod
from typing import List

from .exceptions import (
    PortfolioDoesNotExist,
)
from .domain import (
    Portfolio,
    PortfolioMember,
)


class PortfolioStorage(ABC):

    @abstractmethod
    def create(self, portfolio: Portfolio) -> Portfolio:
        pass


class PortfolioMembershipStorage(ABC):
    PortfolioDoesNotExist = PortfolioDoesNotExist

    @abstractmethod
    def add_member(self, member: PortfolioMember, portfolio: Portfolio):
        pass

    @abstractmethod
    def list_portfolios(self, member: PortfolioMember) -> List[Portfolio]:
        pass
