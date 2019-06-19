import pytest

from src import interfaces
from src.domain import Stock
from src.operations import (
    AddStockOperation,
    ListStocksOperation,
)
from src.storages.memory import StockMemoryStorage


@pytest.fixture
def reader():
    class FakeReader(interfaces.StockReader):
        def read_stocks(self):
            return [
                Stock(symbol='GOOG1', name='Google Inc.'),
                Stock(symbol='GOOG2', name='Google Inc.'),
                Stock(symbol='GOOG3', name='Google Inc.'),
            ]
    return FakeReader()


@pytest.fixture
def storage():
    return StockMemoryStorage()


@pytest.fixture
def add_stock(storage, reader):
    return AddStockOperation(storage, reader)


@pytest.fixture
def list_stocks(storage):
    return ListStocksOperation(storage)
