from typing import Optional
from dataclasses import dataclass

from src.investors import portfolio


@dataclass
class Portfolio(portfolio.Portfolio):
    pass


@dataclass
class Stock:
    portfolio: Portfolio
    symbol: str
    id: Optional[int] = None
