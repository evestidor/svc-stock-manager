from .domain import Portfolio
from .exceptions import PortfolioDoesNotExist
from .interfaces import PortfolioStorage


class MemoryPortfolioStorage(PortfolioStorage):
    DoesNotExist = PortfolioDoesNotExist

    def __init__(self):
        self._db = {}

    def create(self, portfolio: Portfolio) -> Portfolio:
        portfolio.id = self._create_id(portfolio)
        self._db[portfolio.user_id] = portfolio
        return portfolio

    def get_by_user_id(self, user_id: int) -> Portfolio:
        try:
            return self._db[user_id]
        except KeyError:
            raise self.DoesNotExist

    def _create_id(self, portfolio: Portfolio) -> int:
        return id(portfolio)
