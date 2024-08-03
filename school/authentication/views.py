from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import CreateChannel
from .serializers import CreateChannelSerializer, SignInSerializer

@api_view(['POST'])
def create_channel(request):
    serializer = CreateChannelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "message": "Channel has been created", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"status": "failure", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sign_in(request):
    serializer = SignInSerializer(data=request.data)
    if serializer.is_valid():
        try:
            channel = CreateChannel.objects.get(channel_email=serializer.validated_data['channel_email'])
            if check_password(serializer.validated_data['channel_password'], channel.channel_password):
                return Response({"status": "success", "message": "Sign-in successful", "data": {"channel_name": channel.channel_name, "channel_email": channel.channel_email}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "failure", "message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
        except CreateChannel.DoesNotExist:
            return Response({"status": "failure", "message": "Channel does not exist"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"status": "failure", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
