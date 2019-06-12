import datetime

from src import interfaces
from src.domain import (
    Stock,
    StockLot,
)


class AddStockLotOperation(interfaces.Operation):

    def __init__(self, storage: interfaces.LotStorage):
        self._storage = storage

    def execute(
        self,
        stock: Stock,
        quantity: int,
        cost: float,
        date: datetime.date,
    ):
        lot = StockLot(
            stock=stock,
            quantity=quantity,
            cost=cost,
            date=date,
        )
        return self._storage.add(lot)
