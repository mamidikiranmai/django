from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Userid','name','password','email','MobileNumber']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    Userid = UserSerializer()
    Postid  = PostSerializer()
    class Meta:
        model = Like
        fields = ['Userid','Postid','Likeid','comment']

