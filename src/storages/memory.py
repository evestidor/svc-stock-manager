from typing import List

from src.domain import Stock
from src.exceptions import StockAlreadyExists
from src.interfaces import StockStorage


class StockMemoryStorage(StockStorage):
    AlreadyExists = StockAlreadyExists

    def __init__(self):
        self._db = {}

    def add(self, stock: Stock) -> Stock:
        stock = self._clone_stock(stock)

        if self._does_stock_exist(stock):
            raise self.AlreadyExists

        self._db[stock.symbol] = stock
        return stock

    def list(self) -> List[Stock]:
        return list(self._db.values())

    def _clone_stock(self, stock: Stock) -> Stock:
        return Stock(**stock.__dict__)

    def _does_stock_exist(self, stock: Stock) -> bool:
        return stock.symbol in self._db
