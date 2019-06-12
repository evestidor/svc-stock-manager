from django.db import models


class Stock(models.Model):
    symbol = models.CharField(unique=True, max_length=255)
