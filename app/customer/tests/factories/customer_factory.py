from factory.django import DjangoModelFactory

from customer.models import Customer


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = "Alejandro Suau Ruiz"
    address = "Carrer de Girona, 90, 08009 Barcelona"
    email = "alejandro.suau@gmail.com"
    phone = "+34 600676767"
