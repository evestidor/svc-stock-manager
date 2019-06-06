from ..domain import Portfolio
from ..abstract import PortfolioStorage


class MemoryStorage(PortfolioStorage):

    def __init__(self):
        self._db = {}

    def create_portfolio(self, portfolio: Portfolio) -> Portfolio:
        portfolio = self._clone_portfolio(portfolio)
        portfolio.id = id(portfolio)
        self._db[portfolio.account_id] = portfolio
        return portfolio

    def get_by_account_id(self, account_id: int) -> Portfolio:
        try:
            return self._db[account_id]
        except KeyError:
            raise self.DoesNotExist

    def _clone_portfolio(self, portfolio: Portfolio):
        return Portfolio(**portfolio.__dict__)
