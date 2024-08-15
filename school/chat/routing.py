from django.urls import path
from .consumers import ChatroomConsumer, OnlineStatusConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:group_id>/', ChatroomConsumer.as_asgi()),
    path('ws/status/', OnlineStatusConsumer.as_asgi()),
]
