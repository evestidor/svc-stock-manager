import pytest

from src.portfolios import (
    Portfolio,
    PortfolioManager,
)
from src.portfolios.storages.memory import MemoryStorage


class BaseTestHelper:

    def setup_method(self, method):
        self.portfolio_manager = PortfolioManager(MemoryStorage())

    def _create_portfolio(self):
        return self.portfolio_manager.create_portfolio(1)

    def _get_portfolio_by_account(self):
        return self.portfolio_manager.get_portfolio_by_account(1)


class TestCreatePortfolio(BaseTestHelper):

    def test_returns_portfolio_instance(self):
        result = self._create_portfolio()
        assert isinstance(result, Portfolio)

    def test_can_create_multiple_portfolios(self):
        self._create_portfolio()
        self._create_portfolio()


class TestGetPortfolioByAccount(BaseTestHelper):

    def test_returns_portfolio_instance(self):
        self._create_portfolio()
        result = self._get_portfolio_by_account()
        assert isinstance(result, Portfolio)

    def test_when_no_portfolio_raises_does_not_exist(self):
        with pytest.raises(self.portfolio_manager.DoesNotExist):
            self._get_portfolio_by_account()
