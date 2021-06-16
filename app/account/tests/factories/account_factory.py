import factory
from factory.django import DjangoModelFactory

from account.models import Currency, Account

from customer.tests.factories.customer_factory import CustomerFactory


class CurrencyFactory(DjangoModelFactory):
    class Meta:
        model = Currency

    name = "EURO"
    abbreviation = "EUR"
    symbol = "€"


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    internal_identifier = 1
    name = "Cuenta corriente"
    number = "ES9121000418450200051332"
    balance = 100.00
    currency = factory.SubFactory(CurrencyFactory)
    customer = factory.SubFactory(CustomerFactory)
