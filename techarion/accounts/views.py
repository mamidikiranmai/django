from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel,UserCartModel,UserCartProductModel
from .serializers import UserModelserializer,UserCartProductModelserializer,UserCartModelserializer
from rest_framework.utils import json
# Create your views here.
class RegistrationAPI(generics.GenericAPIView):
    serializer_class = UserModelserializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        print("hai")
        return Response(UserModelserializer(user).data)

class GetMemberAPI(APIView):
    serializer_class = UserModelserializer

    def get(self, request):
        queryset= UserModel.objects.all()
        recserializer = UserModelserializer(queryset,many=True)
        return Response(recserializer.data)

class UserCartProductModelAPI(generics.GenericAPIView):
    serializer_class = UserCartProductModelserializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        print("hai")
        return Response(UserCartProductModelserializer(user).data)

class UserCartModelAPI(generics.GenericAPIView):
    serializer_class = UserCartModelserializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        print("hai")
        return Response(UserCartModelserializer(user).data)
class GetUserCartProductModelAPI(APIView):
    serializer_class = UserCartProductModelserializer

    def get(self, request):
        queryset= UserCartProductModel.objects.all()
        recserializer = UserCartProductModelserializer(queryset,many=True)
        return Response(recserializer.data)

class GetUserCartModelAPI(APIView):
    serializer_class = UserCartModelserializer

    def get(self, request):
        queryset= UserCartModel.objects.all()
        recserializer = UserCartModelserializer(queryset,many=True)
        return Response(recserializer.data)

