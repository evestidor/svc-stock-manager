from django.db import models


class Stock(models.Model):
    symbol = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=24,
        decimal_places=2,
        null=True,
        blank=True,
    )
