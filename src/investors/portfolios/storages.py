from typing import List
from collections import defaultdict

from .domain import (
    Portfolio,
    PortfolioMember,
)
from .exceptions import PortfolioDoesNotExist
from .interfaces import (
    PortfolioStorage,
    PortfolioMembershipStorage,
)


class MemoryPortfolioStorage(PortfolioStorage):
    DoesNotExist = PortfolioDoesNotExist

    def __init__(self):
        self._db = []

    def create(self, portfolio: Portfolio) -> Portfolio:
        portfolio = self._clone_portfolio(portfolio)
        portfolio.id = id(portfolio)
        self._db.append(portfolio)
        return portfolio

    def _clone_portfolio(self, portfolio: Portfolio):
        return Portfolio(**portfolio.__dict__)


class MemoryPortfolioMembershipStorage(PortfolioMembershipStorage):

    def __init__(self):
        self._db = defaultdict(list)

    def add_member(self, member: PortfolioMember, portfolio: Portfolio):
        self._db[member.id].append(portfolio)

    def list_portfolios(self, member: PortfolioMember) -> List[Portfolio]:
        return self._db[member.id]
