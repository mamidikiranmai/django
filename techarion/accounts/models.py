from django.db import models
#from Products.models import productMainModel
# Create your models here.
class UserModel(models.Model):
    Phone_number=models.CharField(max_length=12,unique=True)
    Email=models.EmailField(max_length=100)
    is_customer=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    objects = models.manager

class model(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'
        OTHERS = 'OTHERS'
    Phone_number = models.CharField(max_length=12, unique=True)
    Email = models.EmailField(max_length=100)
    Date_of_birth = models.DateField()
    Gender = models.CharField(max_length=200, choices=Gender.choices)
    Image = models.ImageField()

class userProfileModel(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'
        OTHERS = 'OTHERS'
    owner=models.OneToOneField(UserModel,related_name="user",on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Date_of_birth=models.DateField()
    Gender = models.CharField(max_length=200, choices=Gender.choices)
    Image=models.ImageField()
    objects = models.manager

class userloginotpModel(models.Model):
    owner= models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='UserModel')
    Otp= models.IntegerField()
    active=models.BooleanField(default=False)
    objects = models.manager

class UserCartProductModel(models.Model):
    class Status(models.TextChoices):
        pending = 'pending'
        completed = 'completed'

    owner= models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='UserModels')
    product=models.ForeignKey('Product.productMainModel', on_delete=models.CASCADE, related_name='productMainModel')
    Gender = models.CharField(max_length=200, choices=Status.choices)
    objects = models.manager

class UserCartModel(models.Model):
    owner= models.OneToOneField(UserModel,on_delete=models.CASCADE,related_name="users")
    products=models.ManyToManyField('UserCartProductModel',related_name='UserCartProductModel')
    price=models.IntegerField()
    objects = models.manager