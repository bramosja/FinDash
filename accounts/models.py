from django.db import models

ACCOUNT_TYPE_CHOICES = (

)

class Account(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100, choices=ACCOUNT_TYPE_CHOICES)

class Balance(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_time = models.DateTimeField()

class Change(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    change_amount = models.DecimalField(max_digits=10, decimal_places=2)
