import pytest

from src.stock_manager import (
    AddStockOperation,
    ListStocksOperation,
)
from src.stock_manager.storages.memory import StockMemoryStorage


@pytest.fixture
def storage():
    return StockMemoryStorage()


@pytest.fixture
def add_stock(storage):
    return AddStockOperation(storage)


@pytest.fixture
def list_stocks(storage):
    return ListStocksOperation(storage)
