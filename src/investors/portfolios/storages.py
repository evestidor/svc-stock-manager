from .domain import (
    Account,
    Portfolio,
)
from .exceptions import PortfolioDoesNotExist
from .interfaces import PortfolioStorage


class MemoryPortfolioStorage(PortfolioStorage):
    DoesNotExist = PortfolioDoesNotExist

    def __init__(self):
        self._db = {}

    def create(self, portfolio: Portfolio) -> Portfolio:
        portfolio.id = self._create_id(portfolio)
        self._db[portfolio.account.id] = portfolio
        return portfolio

    def get_by_account(self, account: Account) -> Portfolio:
        try:
            return self._db[account.id]
        except KeyError:
            raise self.DoesNotExist

    def _create_id(self, portfolio: Portfolio) -> int:
        return id(portfolio)
