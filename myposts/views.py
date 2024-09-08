from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from posts.models import Post
from posts.serializers import PostsSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
# Create your views here.

class GetPostsView(APIView):
    def post(self,request):
        id = request.data.get('channel_id')
        try:
            posts = Post.objects.filter(channel_id = id)
            serializer = PostsSerializer(posts,many = True)
            return Response({"status":"success","message":serializer.data}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"status":"failure","error":"not found"}, status=status.HTTP_404_NOT_FOUND)

            

