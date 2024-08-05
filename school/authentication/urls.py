from django.urls import path
from .views import signup, signin, user_logout, verify_code, get_user_profile

urlpatterns = [
    path('createchannel/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', user_logout, name='logout'),
    path('verify/', verify_code, name='verify_code'),
    path('user-profile/', get_user_profile, name='get_user_profile'),
]
