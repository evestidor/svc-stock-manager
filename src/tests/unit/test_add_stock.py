import pytest

from src.domain import Stock
from src.exceptions import StockAlreadyExists


class TestCreate:

    def test_returns_stock_instance(
        self,
        add_stock,
    ):
        result = add_stock.execute(symbol='GOOG1')
        assert isinstance(result, Stock)

    def test_can_add_multiple_stocks(
        self,
        add_stock,
    ):
        add_stock.execute(symbol='GOOG1')
        add_stock.execute(symbol='GOOG2')

    def test_when_adding_same_stock_twice_raises_already_exists(
        self,
        add_stock,
    ):
        with pytest.raises(StockAlreadyExists):
            add_stock.execute(symbol='GOOG1')
            add_stock.execute(symbol='GOOG1')
