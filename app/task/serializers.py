from rest_framework import serializers

from app.tasks import parse_accounts

from .models import Task

from account.serializers import AccountSerializer
from customer.serializers import CustomerSerializer
from statement.serializers import StatementSerializer


class TaskSerializer(serializers.ModelSerializer):
    celery_task_id = serializers.UUIDField(default=None, read_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("status",)

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        celery_task_id = parse_accounts.delay(username, password).id
        validated_data["celery_task_id"] = celery_task_id

        return Task.objects.create(celery_task_id=celery_task_id)


class TaskDetailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    account = AccountSerializer(many=True, read_only=True,
                                source="account_set")
    statement = StatementSerializer(many=True, read_only=True,
                                    source="statement_set")

    class Meta:
        model = Task
        fields = ("id", "celery_task_id", "status",
                  "account", "customer", "statement")
        read_only_fields = ("status",)
