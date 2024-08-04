from django.urls import path 
from . import views
urlpatterns = [
    
    path('createchannel/',views.createChannel),
    path('forgetpassword/',views.chackEmailForgetPassword),
    path('checkverifycode/',views.checkVerifyCode),
    path('recivemypassword/',views.recivemypassword),
  




  


]
