from django.contrib import admin
from django.urls import path,include
from .views import  RegistrationProductAPI,GetMemberProductAPI,ProductAPI,GetProductAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegistrationProductAPI.as_view(),name='register'),
    path('registerget/',GetMemberProductAPI.as_view(),name='getregister'),
    path('ProductAPI/',ProductAPI.as_view(),name='register'),
    path('GetProductAPI/',GetProductAPI.as_view(),name='getregister'),
    ]