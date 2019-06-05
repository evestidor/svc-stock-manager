from src.investors.portfolios import (
    MemoryPortfolioMembershipStorage,
    Portfolio,
    PortfolioMember,
    PortfolioMembershipManager,
)


class BaseTestHelper:

    def setup_method(self, method):
        self.member = PortfolioMember(id=1)
        self.membership_manager = PortfolioMembershipManager(
            MemoryPortfolioMembershipStorage()
        )

    def _add_member(self, portfolio: Portfolio):
        return self.membership_manager.add_member(self.member, portfolio)

    def _list_portfolios(self):
        return self.membership_manager.list_portfolios(self.member)


class TestAddMember(BaseTestHelper):

    def test_can_add_member_to_portfolio(self):
        self._add_member(Portfolio(id=1))


class TestListPortfolios(BaseTestHelper):

    def test_when_no_membership_returns_empty_list(self):
        result = self._list_portfolios()
        assert result == []

    def test_returns_list_of_portfolios(self):
        portfolio_1 = Portfolio(id=1)
        portfolio_2 = Portfolio(id=2)

        self._add_member(portfolio_1)
        self._add_member(portfolio_2)

        result = self._list_portfolios()
        assert result == [portfolio_1, portfolio_2]
