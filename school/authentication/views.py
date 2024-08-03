
from django.http import JsonResponse

from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CreateChannel
from .serializers import CreateChannelSerializer
from django.contrib.auth.hashers import make_password
@api_view(['POST'])
def createChannel(request):
    
    serializer = CreateChannelSerializer(data= request.data)
    
    if serializer.is_valid():
        channel = CreateChannel(
            channel_name = serializer.validated_data["channel_name"],
            channel_email = serializer.validated_data["channel_email"],
            channel_password =make_password(serializer.validated_data["channel_password"]) ,
            channel_phone = serializer.validated_data["channel_phone"],
            channel_desc = serializer.validated_data["channel_desc"],
            channel_img = serializer.validated_data["channel_img"],
            channel_likes = serializer.validated_data["channel_likes"],
            channel_type = serializer.validated_data["channel_type"],
            channel_verifycode = serializer.validated_data["channel_verifycode"],
            channel_approve = serializer.validated_data["channel_approve"],
            
        )
        channel.save()
        return JsonResponse({"status":"success","message":"channel has been created","data":serializer.validated_data})
    return JsonResponse({"status":"failure","message":serializer.errors})







        

