from abc import ABC, abstractmethod
from typing import List

from .domain import (
    Stock,
    Portfolio,
)
from .exceptions import StockAlreadyExists


class StockStorage(ABC):
    AlreadyExists = StockAlreadyExists

    @abstractmethod
    def create(self, stock: Stock) -> Stock:
        pass

    @abstractmethod
    def list_by_portfolio(self, portfolio: Portfolio) -> List[Stock]:
        pass
