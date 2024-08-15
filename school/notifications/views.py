# notifications/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notification_list(request):
    user = request.user
    notifications = Notification.objects.filter(user=user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
