import datetime

from .abstract import AbstractOperation

from ..domain import Stock, StockLot
from ..storages.abstract import LotStorage


class AddStockLotOperation(AbstractOperation):

    def __init__(self, storage: LotStorage):
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
