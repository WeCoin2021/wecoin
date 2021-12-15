from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Crypto(models.Model):
    ticker = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=12, decimal_places=5, default=Decimal('0.0000'))
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.ticker
    def __str__(self):
        return str(self.quantity)    

class Store(models.Model):
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    moneyowner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return str(self.credit)

class Transaction_history(models.Model):
    ticker = models.CharField(max_length=10)
    type = models.CharField(max_length=4 ,null=True, blank=False)
    quantity = models.DecimalField(max_digits=14, decimal_places=5, default=Decimal('0.0000'),null=True, blank=False)
    Money_perone = models.DecimalField(max_digits=14, decimal_places=5, default=Decimal('0.0000'),null=True, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.ticker
    def __str__(self):
        return self.type        
    def __str__(self):
        return str(self.quantity)
    def __str__(self):
        return str(self.Money_perone)
    def __str__(self):
        return str(self.time) 


            