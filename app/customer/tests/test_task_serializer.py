from django.test import TestCase

from .factories.customer_factory import CustomerFactory

from customer.serializers import CustomerSerializer


class CustomerSerializerTests(TestCase):
    def test_serializer_customer(self):
        customer = CustomerFactory()
        serializer = CustomerSerializer(customer)

        self.assertTrue(serializer.data.items() <= vars(customer).items())
