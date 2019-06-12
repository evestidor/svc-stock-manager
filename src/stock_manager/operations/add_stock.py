from .abstract import AbstractOperation
from ..storages.abstract import StockStorage
from ..domain import Stock


class AddStockOperation(AbstractOperation):

    def __init__(self, storage: StockStorage):
        self._storage = storage

    def execute(self, symbol: str) -> Stock:
        stock = Stock(symbol=symbol)
        return self._storage.add(stock)
