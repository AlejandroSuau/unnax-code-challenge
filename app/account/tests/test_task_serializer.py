from django.test import TestCase

from .factories.account_factory import AccountFactory

from account.serializers import AccountSerializer


class AccountSerializerTests(TestCase):
    def test_serializer_account(self):
        account = AccountFactory()
        serializer = AccountSerializer(account)

        self.assertIsNotNone(serializer.data)
