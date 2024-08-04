
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CreateChannel 
from .serializers import CreateChannelSerializer 
from django.contrib.auth.hashers import make_password
import random
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


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
            channel_verifycode =str(random.randint(100000,999999)) ,
            channel_approve = serializer.validated_data["channel_approve"],
            
        )
        channel.save()
        return JsonResponse({"status":"success","message":"channel has been created","data":serializer.validated_data})
    return JsonResponse({"status":"failure","message":serializer.errors})


@api_view(['POST'])
def chackEmailForgetPassword(request):
    try:
        email = CreateChannel.objects.get(channel_email = request.data["channel_email"])
        
        serializer = CreateChannelSerializer(email)
        verifycode = serializer.data["channel_verifycode"]
        print(verifycode)
        
        send_mail(
            'Hello, Check Email to recive password',
            f'Your Verify code is : {verifycode}',
            settings.EMAIL_HOST_USER,
            ['onechot20042020@gmail.com']

        )


      

        return JsonResponse({"status":"success","message":"Email is exist"})
    except CreateChannel.DoesNotExist:
        return JsonResponse({"status":"failure","message":"Email not exist"})



@api_view(['POST'])
def checkVerifyCode(request):
    try:
        data = CreateChannel.objects.get(channel_verifycode = request.data['channel_verifycode'])
        if not data:
            return JsonResponse({"status":"failure","message":"verify code can't be null"})
        data.channel_approve = True
        data.save()
        serializer = CreateChannelSerializer(data)
        return JsonResponse({"status":'success'})


    except CreateChannel.DoesNotExist:
        return JsonResponse({"status":'failure',"message":"verify code is wrong please check your email again."})




api_view(['POST'])
def recivemypassword(request):
    try:
        data = CreateChannel.objects.get(channel_email = request.data["channel_email"])
        if not data:
            return JsonResponse({"status":"failure","message":"verify code can't be null"})
        data.channel_password = make_password(request.data['channel_password'])
        data.save()
        serializer = CreateChannelSerializer(data)
        return JsonResponse({"status":'success'})
    except CreateChannel.DoesNotExist:
        return JsonResponse({"status":'failure','message':"chan't recive password"})

