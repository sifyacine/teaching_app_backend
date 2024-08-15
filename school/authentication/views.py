from django.contrib.auth import authenticate, logout
from django.core.mail import send_mail
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Channel
from .serializers import ChannelSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import random
from rest_framework_simplejwt.tokens import RefreshToken
import logging


@api_view(['GET'])
def get_user_profile(request):
    email = request.query_params.get('channel_email')
    
    if not email:
        return Response({'error': 'No email provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Channel.objects.get(channel_email=email)
        serializer = ChannelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Channel.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error during get user profile: {e}")
        return Response({'error': 'An error occurred while fetching user profile'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def signup(request):
    data = request.data
    serializer = ChannelSerializer(data=data)
    if serializer.is_valid():
        channel = serializer.save()
        
        # Generate and save the verification code
        verify_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        channel.channel_verifycode = verify_code
        
        # Save the uploaded image
        channel_img = request.FILES.get('channel_img')
        if channel_img:
            channel.channel_img.save(channel_img.name, channel_img)
        
        channel.save()

        # Send verification email
        send_mail(
            'Your verification code',
            f'Your verification code is {verify_code}',
            'from@example.com',
            [channel.channel_email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



logger = logging.getLogger(__name__)

@api_view(['POST'])
def signin(request):
    data = request.data
    email = data.get('channel_email')
    password = data.get('channel_password')

    logger.info(f"Received signin request for email: {email}")

    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Authenticate user using email and password
        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': 'User account is inactive'}, status=status.HTTP_403_FORBIDDEN)

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error during signin: {e}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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
