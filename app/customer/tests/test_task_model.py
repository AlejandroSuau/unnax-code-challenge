from django.test import TestCase

from .factories.customer_factory import CustomerFactory

from customer.models import Customer


class CustomerModelTests(TestCase):
    def test_create_customer_model(self):
        customer = CustomerFactory()

        customers = Customer.objects.all()

        self.assertEqual(customers.count(), 1)
        self.assertEqual(customers.get().name, customer.name)
