

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.models import Channel
from authentication.serializers import ChannelSerializer
from .models import Post 

from .serializers import PostsSerializer ,PostImagesSerializer

from django.shortcuts import get_object_or_404


class CreatePost(APIView):
    def post(self, request, format=None):
        serializer = PostsSerializer(data=request.data)
        
        if serializer.is_valid():
            post = serializer.save()
            

            channel  = Channel.objects.get(id = request.data['channel'])
            secondSerializer = ChannelSerializer(channel)    
            images = request.FILES.getlist('images')

            for image in images:
                image_serializer = PostImagesSerializer(data={'post': post.id, 'channel':request.data['channel'] ,'image': image})
                if image_serializer.is_valid():
                    image_serializer.save()
                else:
                    # تعامل مع الأخطاء في حفظ الصورة
                    return Response({"status":"failure","error":"image not correct"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"status": "success", "message": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status":"failure","error":f"{serializer.errors} the post has not been created because the title of the post is than 800 characters"}, status=status.HTTP_400_BAD_REQUEST)
class GetPost(APIView):
    def post(self , request):
        id = request.data.get('id')
        try:
             post = get_object_or_404(Post.objects.prefetch_related('images','likes','comments'),pk = id)
             serializer = PostsSerializer(post)
             return Response({"status":"success","message":serializer.data}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
             return Response({"status":"failure","error":"post not found"},status=status.HTTP_404_NOT_FOUND)



class UpdatePost(APIView):

    def post(self, request):
        try:
            post = Post.objects.get(pk=request.data.get('id'))
        except Post.DoesNotExist:
            return Response({"status":"failure" , 'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

     

        serializer = PostsSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({'status':'success','data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeletePost(APIView):
    def post(self,request):
        post_id = request.data['id']
        if not post_id:
            return JsonResponse({'status':'failure','messgae':"id is nesscery for delete post"})
        try:    
            post = Post.objects.get(id = post_id)
        except Post.DoesNotExist:
            return Response({'status':'failure','messgae':"this post has not been founded in the database"})
        post.delete()
        return Response({'status':'success'},status=status.HTTP_200_OK)
    
