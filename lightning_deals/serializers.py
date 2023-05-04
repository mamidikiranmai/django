from rest_framework import serializers
from .models import LightningDeal, Order

class LightningDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightningDeal
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'