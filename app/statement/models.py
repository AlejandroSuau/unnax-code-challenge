from django.db import models

from account.models import Account
from task.models import Task


class Statement(models.Model):
    class Type(models.TextChoices):
        DEPOSIT = "DEPOSIT", "Deposit"
        WITHDRAW = "WITHDRAW", "Withdraw"

    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    concept = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=Type.choices)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        _amount = self.amount
        if self.type == self.Type.WITHDRAW:
            _amount = f"-{_amount}"

        return (
            f"\t"
            f"{self.date:^10}|"
            f"{_amount:^10}|"
            f"{self.balance:^10}| "
            f"{self.concept}"
        )
