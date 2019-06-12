from src import interfaces
from src.domain import Stock


class AddStockOperation(interfaces.Operation):

    def __init__(self, storage: interfaces.StockStorage):
        self._storage = storage

    def execute(self, symbol: str) -> Stock:
        stock = Stock(symbol=symbol)
        return self._storage.add(stock)
