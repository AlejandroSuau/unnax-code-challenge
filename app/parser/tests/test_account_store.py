from django.test import TestCase

from parser.account_parser import AccountStoreHelper

from statement.tests.factories.statement_factory import StatementFactory
from task.tests.factories.task_factory import TaskFactory

from customer.models import Customer
from account.models import Account
from statement.models import Statement


class TestAccountStore(TestCase):
    def test_store_data(self):
        task = TaskFactory()

        statement = StatementFactory()
        account = statement.account
        customer = account.customer

        accounts = [account]
        statements = [[statement]]

        AccountStoreHelper.store(task, customer, accounts, statements)

        self.assertEqual(customer.task, task)
        self.assertEqual(Customer.objects.all().count(), 1)
        self.assertEqual(Account.objects.all().count(), 1)
        self.assertEqual(Statement.objects.all().count(), 1)
