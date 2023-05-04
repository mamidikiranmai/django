from django.urls import path
from .views import LightningDealList, OrderCreate,LightningDealPost

urlpatterns = [
    path('lightning-deals/', LightningDealList.as_view(), name='lightning-deal-list'),
    path('orders/<int:id>', OrderCreate.as_view(), name='order-create'),
    path('LightningDealPost/', LightningDealPost.as_view(), name='LightningDeal'),
]