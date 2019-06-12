from .abstract import AbstractOperation

from ..storages.abstract import StockStorage


class ListStocksOperation(AbstractOperation):

    def __init__(self, storage: StockStorage):
        self._storage = storage

    def execute(self):
        return self._storage.list()
