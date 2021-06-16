import uuid

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

from task.models import Task

READ_TASK_URL = reverse("task:task-list")


class TestTasksApi(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.api_client = APIClient()

    def test_task_list_empty(self):
        res = self.api_client.get(READ_TASK_URL)

        self.assertEqual(res.data["count"], 0)

    def test_task_list_with_one_task(self):
        Task.objects.create(celery_task_id=uuid.uuid4())
        res = self.api_client.get(READ_TASK_URL)

        self.assertEqual(res.data["count"], 1)
