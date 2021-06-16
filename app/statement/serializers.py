from rest_framework import serializers

from .models import Statement


class StatementSerializer(serializers.ModelSerializer):
    account = serializers.CharField(source="account.name")

    class Meta:
        model = Statement
        fields = ("account", "date", "amount", "balance", "concept", "type")
