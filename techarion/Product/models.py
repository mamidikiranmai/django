import uuid

from django.db import models

# Create your models here.
class productMainModel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Unique_id = models.CharField(max_length=12, unique=True,default=uuid.uuid4())
    Price=models.IntegerField()
    objects = models.manager

class productImageModel(models.Model):
    product= models.ForeignKey(productMainModel, on_delete=models.CASCADE, related_name='UserModel')
    image= models.ImageField()
    objects = models.manager