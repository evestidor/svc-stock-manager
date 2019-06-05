from .domain import (
    Account,
    Portfolio,
)
from .exceptions import PortfolioDoesNotExist
from .interfaces import PortfolioStorage


class PortfolioManager:
    DoesNotExist = PortfolioDoesNotExist

    def __init__(self, storage: PortfolioStorage):
        self._storage = storage

    def create(self, account: Account) -> Portfolio:
        portfolio = Portfolio(account=account)
        return self._storage.create(portfolio)

    def get_by_account(self, account: Account) -> Portfolio:
        return self._storage.get_by_account(account)
