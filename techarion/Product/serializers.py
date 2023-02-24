from  rest_framework import serializers
from .models import *
class productMainModelserializer(serializers.ModelSerializer):
    class Meta:
        model = productMainModel
        fields = "__all__"

class productImageModelserializer(serializers.ModelSerializer):
    class Meta:
        model = productImageModel
        fields = "__all__"