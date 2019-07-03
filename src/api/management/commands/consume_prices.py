import json

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from evestidor_event_stream import EventStream

from src.api.models import Stock as StockModel
from src.operations import UpdateStockPriceOperation
from src.storages.django import StockDjangoStorage
from src.exceptions import StockDoesNotExist


class Command(BaseCommand):
    help = 'Consume new prices from event stream'

    def handle(self, *args, **options):
        handler = EventStream(host='evestidor-event-stream')
        handler.read(
            exchange_name='stock_prices',
            routing_key='stock.prices.update',
            callback=self._handle_new_price,
        )

    def _handle_new_price(self, channel, method, properties, data):
        data = self._parse_data(data)
        try:
            self._execute_operation(data)
            self.stdout.write(self.style.SUCCESS(f'Updated {data}'))
        except StockDoesNotExist:
            self.stdout.write(self.style.WARNING(f'Ignored {data}'))
        except OperationalError:
            self.stdout.write(self.style.WARNING(
                f'Database is down or not migrated'
            ))

    def _parse_data(self, data: str) -> dict:
        return json.loads(data)

    def _execute_operation(self, data: dict):
        storage = StockDjangoStorage(StockModel)
        UpdateStockPriceOperation(storage).execute(
            symbol=data['symbol'],
            price=data['price'],
        )
