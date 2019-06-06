from ..domain import Portfolio
from ..abstract import PortfolioStorage


class DjangoStorage(PortfolioStorage):

    def __init__(self, model):
        self._model = model

    def create_portfolio(self, portfolio: Portfolio) -> Portfolio:
        portfolio = self._clone_portfolio(portfolio)
        portfolio.id = self._store_in_db(portfolio)
        return portfolio

    def get_by_account_id(self, account_id: int) -> Portfolio:
        try:
            return self._model.objects.get(account_id=account_id)
        except self._model.DoesNotExist as e:
            raise self.DoesNotExist from e

    def _clone_portfolio(self, portfolio: Portfolio):
        return Portfolio(**portfolio.__dict__)

    def _store_in_db(self, portfolio: Portfolio) -> int:
        return self._model.objects.create(
            account_id=portfolio.account_id,
        ).id
