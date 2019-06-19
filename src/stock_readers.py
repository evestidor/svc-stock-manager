import json
from typing import List

from src import interfaces
from src.domain import Stock


class JSONStockReader(interfaces.StockReader):

    def __init__(self, path: str):
        self._path = path
        self._cached_json = None

    def read_stocks(self) -> List[dict]:
        if self._cached_json is None:
            self._cached_json = [
                self._parse_stock(data)
                for data in json.loads(open(self._path, 'r+').read())
            ]
        return self._cached_json

    def _parse_stock(self, data: dict) -> Stock:
        return Stock(**data)
