from typing import List

from .domain import (
    Portfolio,
    Stock,
    StockLot,
)
from .exceptions import StockAlreadyExists
from .abstract import StockStorage


class StockManager:
    AlreadyExists = StockAlreadyExists

    def __init__(self, storage: StockStorage):
        self._storage = storage

    def create(
        self,
        portfolio: Portfolio,
        symbol: str,
    ) -> Stock:
        stock = Stock(portfolio=portfolio, symbol=symbol)
        return self._storage.create(stock)

    def list_by_portfolio(self, portfolio: Portfolio) -> List[Portfolio]:
        return self._storage.list_by_portfolio(portfolio)

    def make_investment(self, stock: Stock) -> StockLot:
        return StockLot()
