from src import interfaces
from src.domain import Stock


class ListStockLotsOperation(interfaces.Operation):

    def __init__(self, storage: interfaces.LotStorage):
        self._storage = storage

    def execute(self, symbol: str):
        stock = Stock(symbol=symbol)
        return self._storage.list(stock)
