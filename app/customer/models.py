from django.db import models

from task.models import Task


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return (
            f"Customer Data:\n"
            f"\tName: {self.name}\n"
            f"\tAddress: {self.address}\n"
            f"\tEmail: {self.email}\n"
            f"\tPhone: {self.phone}\n"
        )
