from ..domain import Portfolio
from ..abstract import PortfolioStorage
from ..exceptions import PortfolioDoesNotExist


class PortfolioManager:
    DoesNotExist = PortfolioDoesNotExist

    def __init__(self, storage: PortfolioStorage):
        self._storage = storage

    def create_portfolio(self, account_id: int) -> Portfolio:
        portfolio = Portfolio(account_id=account_id)
        return self._storage.create(portfolio)

    def get_portfolio_by_account(self, account_id: int) -> Portfolio:
        return self._storage.get_by_account_id(account_id)
