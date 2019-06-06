from dataclasses import dataclass
from typing import Optional


@dataclass
class Portfolio:
    account_id: int
    id: Optional[int] = None
