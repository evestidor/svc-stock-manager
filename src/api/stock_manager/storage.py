from typing import List

from stock_manager import (
    Stock,
    StockAlreadyExists,
    StockStorage,
)

from .models import Stock as StockDB


class StockDjangoStorage(StockStorage):
    AlreadyExists = StockAlreadyExists

    def __init__(self, model: StockDB = StockDB):
        self.model = model

    def add(self, stock: Stock) -> Stock:
        instance = self.model(**stock.__dict__)
        instance.save()
        return stock

    def list(self) -> List[Stock]:
        instances = self.model.objects.all()
        stocks = self._queryset_to_domain(instances)
        return stocks

    def _queryset_to_domain(self, instances: List[StockDB]) -> List[Stock]:
        return [Stock(**instance.__dict__) for instance in instances]
