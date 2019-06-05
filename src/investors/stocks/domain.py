from typing import Optional
from dataclasses import dataclass

from src.investors import portfolios


@dataclass
class Portfolio(portfolios.Portfolio):
    pass


@dataclass
class Stock:
    portfolio: Portfolio
    symbol: str
    id: Optional[int] = None


@dataclass
class StockLot:
    pass
