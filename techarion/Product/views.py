from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import productMainModel,productImageModel
from .serializers import productMainModelserializer,productImageModelserializer

class RegistrationProductAPI(generics.GenericAPIView):
    serializer_class = productMainModelserializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        print("hai")
        return Response(productMainModelserializer(user).data)

class GetMemberProductAPI(APIView):
    serializer_class = productMainModelserializer

    def get(self, request):
        queryset= productMainModel.objects.all()
        recserializer = productMainModelserializer(queryset,many=True)
        return Response(recserializer.data)

class ProductAPI(generics.GenericAPIView):
    serializer_class = productImageModelserializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        print("hai")
        return Response(productImageModelserializer(user).data)

class GetProductAPI(APIView):
    serializer_class = productImageModelserializer

    def get(self, request):
        queryset= productImageModel.objects.all()
        recserializer = productImageModelserializer(queryset,many=True)
        return Response(recserializer.data)

