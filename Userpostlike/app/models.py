import uuid

from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class User(models.Model):
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    Userid = models.UUIDField( primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50,validators=[password_regex])
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    objects = models.manager

    def __str__(self):
        return str(self.Userid)

class Post(models.Model):
    PostId = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)
    UserId = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    createddate = models.DateField(auto_now=True)
    objects = models.manager

    def __str__(self):
        return str(self.PostId)

class Like(models.Model):
    Userid = models.ForeignKey(User,related_name='userid',on_delete=models.CASCADE)
    Postid = models.ForeignKey(Post,related_name="post",on_delete=models.CASCADE)
    Likeid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    comment = models.CharField(max_length=50)
    objects = models.manager

    def __str__(self):
        return str(self.Likeid)