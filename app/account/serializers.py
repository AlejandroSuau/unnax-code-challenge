from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source="customer.name")
    currency = serializers.CharField(source="currency.name")

    class Meta:
        model = Account
        fields = ("name", "number", "customer", "balance", "currency")
