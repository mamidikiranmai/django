from  rest_framework import serializers
from .models import *
class UserModelserializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

class userProfileModelserializer(serializers.ModelSerializer):
    class Meta:
        model = userProfileModel
        fields = "__all__"

class userloginotpModelserializer(serializers.ModelSerializer):
    class Meta:
        model = userloginotpModel
        fields = "__all__"


class UserCartProductModelserializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartProductModel
        fields = "__all__"

class UserCartModelserializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartModel
        fields = "__all__"

class mixedserializer(serializers.ModelSerializer):
    class Meta:
        model = model
        fields = ['Phone_number','Name','Date_of_birth','Gender','Image']

