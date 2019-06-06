import pytest

from src.stocks import (
    MemoryStockStorage,
    Portfolio,
    Stock,
    StockLot,
    StockManager,
)


class StockManagerMixin:

    def setup_method(self, method):
        self.portfolio = Portfolio(id=1)
        self.stock_manager = StockManager(MemoryStockStorage())

    def _create_stock(self, *args, **kwargs):
        return self.stock_manager.create(self.portfolio, *args, **kwargs)

    def _make_investment(self, *args, **kwargs):
        return self.stock_manager.make_investment(*args, **kwargs)

    def _list_stocks(self, *args, **kwargs):
        return self.stock_manager.list_by_portfolio(self.portfolio)


class TestCreate(StockManagerMixin):

    def test_returns_stock_instance(self):
        result = self._create_stock(symbol='GOOG1')
        assert isinstance(result, Stock)

    def test_can_creates_multiple_stocks(self):
        self._create_stock(symbol='GOOG1')
        self._create_stock(symbol='GOOG2')

    def test_when_creating_same_stock_twice_raises_already_exists(self):
        with pytest.raises(self.stock_manager.AlreadyExists):
            self._create_stock(symbol='GOOG1')
            self._create_stock(symbol='GOOG1')


class TestListByPortfolio(StockManagerMixin):

    def test_when_no_stocks_returns_empty_list(self):
        result = self._list_stocks()
        expected = []
        assert expected == result

    def test_when_there_are_stocks_returns_list_of_stocks(self):
        stock_1 = self._create_stock(symbol='GOOG1')
        stock_2 = self._create_stock(symbol='GOOG2')
        stock_3 = self._create_stock(symbol='GOOG3')

        result = self._list_stocks()
        expected = [stock_1, stock_2, stock_3]
        assert expected == result


class TestMakeInvestment(StockManagerMixin):

    def test_returns_stock_lot_instance(self):
        stock = self._create_stock(symbol='GOOG')
        result = self._make_investment(stock)
        assert isinstance(result, StockLot)
