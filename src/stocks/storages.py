from typing import List
from collections import defaultdict

from .domain import (
    Stock,
    Portfolio,
)
from .exceptions import StockAlreadyExists
from .abstract import StockStorage


class MemoryStockStorage(StockStorage):
    AlreadyExists = StockAlreadyExists

    def __init__(self):
        self._db = defaultdict(list)

    def create(self, stock: Stock) -> Stock:
        stock = self._clone_stock(stock)
        stock.id = self._create_stock_id(stock)

        if self._does_stock_exist(stock):
            raise self.AlreadyExists

        self._db[stock.portfolio.id].append(stock)
        return stock

    def list_by_portfolio(self, portfolio: Portfolio) -> List[Stock]:
        return list(self._db[portfolio.id])

    def _clone_stock(self, stock: Stock) -> Stock:
        return Stock(**stock.__dict__)

    def _create_stock_id(self, stock: Stock) -> int:
        return id(stock)

    def _does_stock_exist(self, stock: Stock) -> bool:
        existing_stocks = self._db[stock.portfolio.id]
        return any(s.symbol == stock.symbol for s in existing_stocks)
