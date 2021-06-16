import factory
from factory.django import DjangoModelFactory

from account.tests.factories.account_factory import AccountFactory

from statement.models import Statement


class StatementFactory(DjangoModelFactory):
    class Meta:
        model = Statement

    date = "1992-05-10"
    amount = 10.50
    balance = 100.50
    concept = "Dinero ingresado",
    account = factory.SubFactory(AccountFactory)
    type = Meta.model.Type.WITHDRAW
