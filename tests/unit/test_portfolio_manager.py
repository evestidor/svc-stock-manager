import pytest

from src.investors.portfolio import (
    MemoryPortfolioStorage,
    Portfolio,
    PortfolioManager,
)


class PortfolioManagerMixin:

    def setup_method(self, method):
        self.portfolio_manager = PortfolioManager(MemoryPortfolioStorage())

    def _create(self, *args, **kwargs):
        return self.portfolio_manager.create(*args, **kwargs)

    def _get_by_user_id(self, *args, **kwargs):
        return self.portfolio_manager.get_by_user_id(*args, **kwargs)


class TestCreate(PortfolioManagerMixin):

    def test_returns_portfolio_instance(self):
        portfolio = self._create(user_id=1)
        assert isinstance(portfolio, Portfolio)

    def test_creates_multiple_portfolios(self):
        self._create(user_id=1)
        self._create(user_id=2)


class TestGetByUserID(PortfolioManagerMixin):

    def test_returns_portfolio_instance(self):
        self._create(user_id=1)
        portfolio = self._get_by_user_id(1)
        assert isinstance(portfolio, Portfolio)

    def test_when_no_portfolio_raises_does_not_exist(self):
        with pytest.raises(PortfolioManager.DoesNotExist):
            self._get_by_user_id(1)
