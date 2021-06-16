from django.db import models

from customer.models import Customer
from task.models import Task


class Currency(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)


class Account(models.Model):
    internal_identifier = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return (
            f"Account Data:\n"
            f"\t\tName: {self.name}\n"
            f"\t\tNumber: {self.number}\n"
            f"\t\tCurrency: {self.currency.abbreviation}\n"
            f"\t\tBalance: {self.balance}\n"
        )
