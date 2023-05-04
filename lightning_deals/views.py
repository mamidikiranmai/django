from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LightningDeal, Order
from .serializers import LightningDealSerializer, OrderSerializer
from django.utils import timezone
from datetime import date, datetime
class LightningDealPost(generics.GenericAPIView):
    serializer_class = LightningDealSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        print("hai")
        return Response(LightningDealSerializer(user).data)

class LightningDealList(generics.ListAPIView):
    serializer_class = LightningDealSerializer

    def get_queryset(self):
        return LightningDeal.objects.filter(expiry_time__gt=timezone.now())

class OrderCreate(generics.GenericAPIView):
    serializer_class =OrderSerializer
    def post(self, request,id):
        deal = LightningDeal.objects.get(id=id)
        if deal.expiry_time():
            return Response({'detail': 'This deal has expired.'}, status=status.HTTP_400_BAD_REQUEST)
        if deal.available_units <= 0:
            return Response({'detail': 'This deal is sold out.'}, status=status.HTTP_400_BAD_REQUEST)
        deal.available_units -= 1
        deal.save()
        return Response({'detail': 'Your order has been placed.'}, status=status.HTTP_201_CREATED)