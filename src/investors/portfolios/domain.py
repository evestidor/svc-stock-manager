from dataclasses import dataclass
from typing import Optional


@dataclass
class Account:
    id: int


@dataclass
class Portfolio:
    account: Account
    id: Optional[int] = None
