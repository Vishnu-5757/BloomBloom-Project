from django.db import models
from django.contrib.auth.models import User



class Deposit(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

