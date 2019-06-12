from typing import List

from src.domain import Stock
from src.exceptions import StockAlreadyExists
from src.interfaces import StockStorage


class StockDjangoStorage(StockStorage):
    AlreadyExists = StockAlreadyExists

    def __init__(self, model):
        self.model = model

    def add(self, stock: Stock) -> Stock:
        instance = self.model(**stock.__dict__)
        instance.save()
        return stock

    def list(self) -> List[Stock]:
        instances = self.model.objects.all()
        stocks = self._queryset_to_domain(instances)
        return stocks

    def _queryset_to_domain(self, instances) -> List[Stock]:
        return [Stock(**instance.__dict__) for instance in instances]
