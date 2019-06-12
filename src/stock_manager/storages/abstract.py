from abc import ABC, abstractmethod
from typing import List

from ..domain import Stock, StockLot
from ..exceptions import StockAlreadyExists


class StockStorage(ABC):
    AlreadyExists = StockAlreadyExists

    @abstractmethod
    def add(self, stock: Stock) -> Stock:
        pass

    @abstractmethod
    def list(self) -> List[Stock]:
        pass


class LotStorage(ABC):

    @abstractmethod
    def add(self, lot: StockLot) -> StockLot:
        pass

    @abstractmethod
    def list(self, stock: Stock) -> List[StockLot]:
        pass
