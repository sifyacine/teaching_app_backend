from django.urls import path
from .views import create_channel, sign_in

urlpatterns = [
    path('createchannel/', create_channel, name='create-channel'),
    path('signin/', sign_in, name='sign-in'),
]
