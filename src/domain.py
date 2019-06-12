import datetime
from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str


@dataclass
class StockLot:
    stock: Stock
    quantity: int
    cost: float
    date: datetime.date
