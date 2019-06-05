from dataclasses import dataclass
from typing import Optional


@dataclass
class Portfolio:
    user_id: int
    id: Optional[int] = None
