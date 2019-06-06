from typing import List

from .domain import (
    Portfolio,
    PortfolioMember,
)
from .interfaces import (
    PortfolioMembershipStorage,
    PortfolioStorage,
)


class PortfolioManager:

    def __init__(self, storage: PortfolioStorage):
        self._storage = storage

    def create(self) -> Portfolio:
        portfolio = Portfolio()
        return self._storage.create(portfolio)


class PortfolioMembershipManager:

    def __init__(self, storage: PortfolioMembershipStorage):
        self._storage = storage

    def add_member(self, member: PortfolioMember, portfolio: Portfolio):
        self._storage.add_member(member, portfolio)

    def list_portfolios(self, member: PortfolioMember) -> List[Portfolio]:
        return self._storage.list_portfolios(member)
