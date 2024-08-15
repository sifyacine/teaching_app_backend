from django.urls import path
from .views import signup, signin, user_logout, verify_code, get_user_profile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('createchannel/', signup, name='create_channel'),
    path('signin/', signin, name='signin'),
    path('logout/', user_logout, name='logout'),
    path('verify/', verify_code, name='verify_code'),
    path('user-profile/', get_user_profile, name='get_user_profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
