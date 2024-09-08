from django.urls import path 
from .views import GetPostsView

urlpatterns = [

    path('get/',GetPostsView.as_view()),
   
]