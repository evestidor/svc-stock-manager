import pytest

from src.investors.portfolios import (
    Account,
    MemoryPortfolioStorage,
    Portfolio,
    PortfolioManager,
)


class PortfolioManagerMixin:

    def setup_method(self, method):
        self.account = Account(id=1)
        self.portfolio_manager = PortfolioManager(MemoryPortfolioStorage())

    def _create_portfolio(self, *args, **kwargs):
        return self.portfolio_manager.create(*args, **kwargs)

    def _get_by_account(self, *args, **kwargs):
        return self.portfolio_manager.get_by_account(*args, **kwargs)


class TestCreate(PortfolioManagerMixin):

    def test_returns_portfolio_instance(self):
        portfolio = self._create_portfolio(self.account)
        assert isinstance(portfolio, Portfolio)

    def test_creates_multiple_portfolios(self):
        self._create_portfolio(self.account)
        self._create_portfolio(self.account)


class TestGetByAccount(PortfolioManagerMixin):

    def test_returns_portfolio_instance(self):
        self._create_portfolio(self.account)
        portfolio = self._get_by_account(self.account)
        assert isinstance(portfolio, Portfolio)

    def test_when_no_portfolio_raises_does_not_exist(self):
        with pytest.raises(PortfolioManager.DoesNotExist):
            self._get_by_account(self.account)
