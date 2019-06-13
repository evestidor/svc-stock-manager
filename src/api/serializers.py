from rest_framework import serializers


class StockSerializer(serializers.Serializer):
    symbol = serializers.CharField()
