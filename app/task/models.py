from django.db import models


class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        DONE = "DONE", "Done"
        FAILED = "ERROR", "Error"

    celery_task_id = models.UUIDField(max_length=50, unique=True,
                                      db_index=True)
    status = models.CharField(max_length=15, choices=Status.choices,
                              default=Status.PENDING)
