from rest_framework import serializers


class StockSerializer(serializers.Serializer):
    symbol = serializers.CharField()
    name = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()
