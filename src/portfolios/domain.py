from dataclasses import dataclass
from typing import Optional


@dataclass
class Portfolio:
    id: Optional[int] = None


@dataclass
class PortfolioMember:
    id: int
