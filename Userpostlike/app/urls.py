from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('UserPost/',Userpost.as_view(),name="UserPost"),
    path("PostPost/",Postpost.as_view(),name="Postpost"),
    path("likepost/",Likepost.as_view(),name="Likepost"),
    path("UserGetAll/",UserGetAll.as_view(),name='UserGetAll'),
    path("UserGetById/<str:Userid>/",UserGetById.as_view(),name="UserGetById"),
    path("UserUpdate/<str:Userid>/",UserUpdate.as_view(),name="UserUpdate"),
    path("UserDelete/<str:Userid>/",UserDelete.as_view(),name="UserDelete"),
    path("PostGetLike/<str:PostId>/",PostGetLike.as_view(),name="PostGetLike"),
    path("PostGetById/<str:PostId>/",PostGetById.as_view(),name="PostGetById"),
    path("PostUpdate/<str:PostId>/",PostUpdate.as_view(),name="PostUpdate"),
    path("PostDelete/<str:PostId>/",PostDelete.as_view(),name="PostDelete"),
    path("LikeGetById/<str:Likeid>/",LikeGetById.as_view(),name="LikeGetById"),
    path("LikeUpdate/<str:Likeid>/",LikeUpdate.as_view(),name="LikeUpdate"),
    path("LikeDelete/<str:Likeid>/",LikeDelete.as_view(),name="LikeDelete"),
]