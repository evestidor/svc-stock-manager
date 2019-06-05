from src.investors.portfolios import (
    MemoryPortfolioStorage,
    Portfolio,
    PortfolioManager,
)


class BaseTestHelper:

    def setup_method(self, method):
        self.portfolio_manager = PortfolioManager(MemoryPortfolioStorage())

    def _create_portfolio(self, *args, **kwargs):
        return self.portfolio_manager.create(*args, **kwargs)


class TestCreate(BaseTestHelper):

    def test_returns_portfolio_instance(self):
        result = self._create_portfolio()
        assert isinstance(result, Portfolio)

    def test_can_create_multiple_portfolios(self):
        self._create_portfolio()
        self._create_portfolio()
