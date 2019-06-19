from typing import Optional, List

from src import interfaces
from src.domain import Stock
from src.exceptions import StockInvalid


class AddStockOperation(interfaces.Operation):

    def __init__(
        self,
        storage: interfaces.StockStorage,
        reader: interfaces.StockReader,
    ):
        self._storage = storage
        self._reader = reader

    def execute(self, symbol: str) -> Stock:
        stock = self._get_stock_from_reader(symbol)

        if stock is None:
            raise StockInvalid

        return self._storage.add(stock)

    def _get_stock_from_reader(self, symbol: str) -> Optional[Stock]:
        try:
            return self._find_stock(symbol, self._reader.read_stocks())
        except IndexError:
            return None

    def _find_stock(self, symbol: str, stocks: List[Stock]) -> Optional[Stock]:
        return [x for x in stocks if x.symbol == symbol][0]
