

class TestListByPortfolio:

    def test_when_no_stocks_returns_empty_list(
        self,
        list_stocks,
    ):
        result = list_stocks.execute()
        expected = []
        assert expected == result

    def test_when_there_are_stocks_returns_list_of_stocks(
        self,
        add_stock,
        list_stocks,
    ):
        stock_1 = add_stock.execute(symbol='GOOG1')
        stock_2 = add_stock.execute(symbol='GOOG2')
        stock_3 = add_stock.execute(symbol='GOOG3')

        result = list_stocks.execute()
        expected = [stock_1, stock_2, stock_3]
        assert expected == result
