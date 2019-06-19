import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Stock:
    symbol: str
    name: Optional[str] = None
    price: Optional[float] = None


@dataclass
class StockLot:
    stock: Stock
    quantity: int
    cost: float
    date: datetime.date
