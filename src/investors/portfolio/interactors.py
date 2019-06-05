from .domain import Portfolio
from .exceptions import PortfolioDoesNotExist
from .interfaces import PortfolioStorage


class PortfolioManager:
    DoesNotExist = PortfolioDoesNotExist

    def __init__(self, storage: PortfolioStorage):
        self._storage = storage

    def create(self, user_id: int) -> Portfolio:
        portfolio = Portfolio(user_id=user_id)
        return self._storage.create(portfolio)

    def get_by_user_id(self, user_id: int) -> Portfolio:
        return self._storage.get_by_user_id(user_id)
