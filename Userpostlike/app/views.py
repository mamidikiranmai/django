from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response


class Userpost(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        return Response(UserSerializer(user).data)


class UserGetAll(generics.GenericAPIView):
    queryset = UserSerializer

    def get(self, request):
        ser = User.objects.all()
        res = UserSerializer(ser, many=True)
        return Response(res.data)

class UserGetById(generics.GenericAPIView):
    queryset = UserSerializer
    def get(self,request,Userid):
        ser = User.objects.filter(Userid=Userid)
        res = UserSerializer(ser,many=True)
        return Response(res.data)

class UserUpdate(generics.GenericAPIView):
    serializer_class = UserSerializer
    def put(self,request,Userid):
        getres= User.objects.get(Userid=Userid)
        pushres = UserSerializer(getres,data=request.data)
        print("push")
        pushres.is_valid()
        print("valid")
        pushres.save()
        return Response(pushres.data)

class UserDelete(generics.GenericAPIView):
    serializer_class = UserSerializer
    def delete(self,request,Userid):
        delres = User.objects.filter(Userid=Userid)
        delres.delete()
        return HttpResponse("Deleted sucessfull")


class Postpost(generics.GenericAPIView):
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        return Response(PostSerializer(user).data)
class PostGetLike(generics.GenericAPIView):
    queryset =PostLikeSerializer
    def get(self,request,PostId):
        try:
            post = Post.objects.get(PostId=PostId)
            likes = Like.objects.filter(Postid=post)
            serializer = PostLikeSerializer(likes, many=True)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return JsonResponse({'message': 'Post does not exist.'}, status=404)

class PostGetById(generics.GenericAPIView):
    queryset = PostSerializer
    def get(self,request,PostId):
        ser = Post.objects.filter(PostId=PostId)
        res = PostSerializer(ser,many=True)
        return Response(res.data)

class PostUpdate(generics.GenericAPIView):
    serializer_class = PostSerializer
    def put(self,request,PostId):
        getres= Post.objects.get(PostId=PostId)
        pushres = PostSerializer(getres,data=request.data)
        print("push")
        pushres.is_valid()
        print("valid")
        pushres.save()
        return Response(pushres.data)

class PostDelete(generics.GenericAPIView):
    serializer_class = PostSerializer
    def delete(self,request,PostId):
        delres = Post.objects.filter(PostId=PostId)
        delres.delete()
        return HttpResponse("Deleted sucessfull")


class Likepost(generics.GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        return Response(LikeSerializer(user).data)

class LikeGetById(generics.GenericAPIView):
    queryset = LikeSerializer
    def get(self,request,Likeid):
        ser = Like.objects.filter(Likeid=Likeid)
        res = LikeSerializer(ser,many=True)
        return Response(res.data)

class LikeUpdate(generics.GenericAPIView):
    serializer_class = LikeSerializer
    def put(self,request,Likeid):
        getres= Like.objects.get(Likeid=Likeid)
        pushres = LikeSerializer(getres,data=request.data)
        print("push")
        pushres.is_valid()
        print("valid")
        pushres.save()
        return Response(pushres.data)

class LikeDelete(generics.GenericAPIView):
    serializer_class = LikeSerializer
    def delete(self,request,Likeid):
        delres = Like.objects.filter(Likeid=Likeid)
        delres.delete()
        return HttpResponse("Deleted sucessfull")
