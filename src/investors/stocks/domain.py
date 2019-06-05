from typing import Optional
from dataclasses import dataclass


@dataclass
class Portfolio:
    id: int


@dataclass
class Stock:
    portfolio: Portfolio
    symbol: str
    id: Optional[int] = None


@dataclass
class StockLot:
    pass
