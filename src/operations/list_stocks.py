from src import interfaces


class ListStocksOperation(interfaces.Operation):

    def __init__(self, storage: interfaces.StockStorage):
        self._storage = storage

    def execute(self):
        return self._storage.list()
