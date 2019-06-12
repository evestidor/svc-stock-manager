from .abstract import AbstractOperation

from ..domain import Stock
from ..storages.abstract import LotStorage


class ListStockLotsOperation(AbstractOperation):

    def __init__(self, storage: LotStorage):
        self._storage = storage

    def execute(self, symbol: str):
        stock = Stock(symbol=symbol)
        return self._storage.list(stock)
