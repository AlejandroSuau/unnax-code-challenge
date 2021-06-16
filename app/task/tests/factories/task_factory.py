import factory
from factory.django import DjangoModelFactory

from task.models import Task


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    celery_task_id = factory.Faker('uuid4')
