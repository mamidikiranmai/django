from django.contrib import admin
from django.urls import path,include
from .views import  RegistrationAPI,GetMemberAPI,UserCartProductModelAPI,UserCartModelAPI,GetUserCartModelAPI,GetUserCartProductModelAPI
urlpatterns = [
    path('register/',RegistrationAPI.as_view(),name='register'),
    path('get/',GetMemberAPI.as_view(),name='register'),
    path('UserCartProductModelAPI/',UserCartProductModelAPI.as_view(),name='register'),
    path('UserCartModelAPI/',UserCartModelAPI.as_view(),name='register'),
    path('GetUserCartModelAPI/',GetUserCartModelAPI.as_view(),name='register'),
    path('GetUserCartProductModelAPI/',GetUserCartProductModelAPI.as_view(),name='register'),
    ]