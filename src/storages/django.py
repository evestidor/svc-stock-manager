from typing import List

from django.db import IntegrityError
from django.db.models import Model

from src.domain import Stock
from src.exceptions import (
    StockAlreadyExists,
    StockDoesNotExist,
)
from src.interfaces import StockStorage


class StockDjangoStorage(StockStorage):
    AlreadyExists = StockAlreadyExists
    DoesNotExist = StockDoesNotExist

    def __init__(self, model: Model):
        self.model = model

    def add(self, stock: Stock) -> Stock:
        instance = self.model(**stock.__dict__)
        try:
            instance.save()
        except IntegrityError as e:
            raise self.AlreadyExists from e
        return stock

    def list(self) -> List[Stock]:
        instances = self.model.objects.all()
        stocks = self._queryset_to_domain(instances)
        return stocks

    def update_price(self, stock: Stock) -> Stock:
        try:
            instance = self.model.objects.get(symbol=stock.symbol)
        except self.model.DoesNotExist as e:
            raise self.DoesNotExist from e

        instance.price = stock.price
        instance.save(update_fields=['price'])
        return self._instance_to_domain(instance)

    def _queryset_to_domain(self, instances) -> List[Stock]:
        return [self._instance_to_domain(instance) for instance in instances]

    def _instance_to_domain(self, instance) -> Stock:
        return Stock(
            symbol=instance.symbol,
            name=instance.name,
            price=instance.price,
        )
