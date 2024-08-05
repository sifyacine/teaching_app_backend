from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Channel
from .serializers import ChannelSerializer
import random

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = ChannelSerializer(data=data)
    if serializer.is_valid():
        channel = serializer.save()
        verify_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        channel.channel_verifycode = verify_code
        channel.save()
        send_mail(
            'Your verification code',
            f'Your verification code is {verify_code}',
            'from@example.com',
            [channel.channel_email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin(request):
    data = request.data
    email = data.get('channel_email')
    password = data.get('channel_password')

    try:
        user = Channel.objects.get(channel_email=email)
    except Channel.DoesNotExist:
        return Response({'error': 'Email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(password):
        return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)

    if not user.channel_approve:
        return Response({'error': 'Email not verified'}, status=status.HTTP_403_FORBIDDEN)

    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def verify_code(request):
    data = request.data
    code = data.get('verification_code')

    try:
        # Find the channel with the given verification code
        channel = Channel.objects.get(channel_verifycode=code)
        if channel:
            channel.channel_approve = True
            channel.channel_verifycode = ''  # Clear the verification code
            channel.save()
            return Response({'message': 'Verification successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
    except Channel.DoesNotExist:
        return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)