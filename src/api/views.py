from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.exceptions import StockAlreadyExists
from src.operations import (
    AddStockOperation,
    ListStocksOperation,
)
from src.storages.django import StockDjangoStorage

from . import errors
from .serializers import StockSerializer
from .models import Stock


class StockListAPI(APIView):
    serializer_class = StockSerializer

    def get(self, request):
        stocks = ListStocksOperation(self._storage).execute()
        serializer = self.serializer_class(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = self._validate_request(request)

        try:
            AddStockOperation(self._storage).execute(**data)
        except StockAlreadyExists:
            return Response(errors.E001, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_201_CREATED)

    @property
    def _storage(self):
        return StockDjangoStorage(Stock)

    def _validate_request(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
