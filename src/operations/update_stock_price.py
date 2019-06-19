from src import interfaces
from src.domain import Stock


class UpdateStockPriceOperation(interfaces.Operation):

    def __init__(self, storage: interfaces.StockStorage):
        self._storage = storage

    def execute(self, symbol: str, price: float) -> Stock:
        stock = Stock(symbol=symbol, price=price)
        return self._storage.update_price(stock)
