from django.test import TestCase

from .factories.account_factory import AccountFactory

from account.models import Account


class CustomerModelTests(TestCase):
    def test_create_customer_model(self):
        account = AccountFactory()

        accounts = Account.objects.all()

        self.assertEqual(accounts.count(), 1)
        self.assertEqual(accounts.get().name, account.name)
