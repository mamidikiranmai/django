from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
class LightningDeal(models.Model):
    product_name = models.CharField(max_length=255)
    actual_price = models.DecimalField(max_digits=8, decimal_places=2)
    final_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_units = models.IntegerField()
    available_units = models.IntegerField()
    expiry_time = models.DateTimeField()
    objects = models.manager

    def __str__(self):
        return str(self.expiry_time)

class Order(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    lightning_deal = models.ForeignKey(LightningDeal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)