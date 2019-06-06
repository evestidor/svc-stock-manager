from ..domain import Portfolio
from ..abstract import PortfolioStorage


class PortfolioManager:

    def __init__(self, storage: PortfolioStorage):
        self._storage = storage

    def create_portfolio(self, account_id: int) -> Portfolio:
        portfolio = Portfolio(account_id=account_id)
        return self._storage.create_portfolio(portfolio)

    def get_portfolio(self, account_id: int) -> Portfolio:
        return self._storage.get_by_account_id(account_id)
