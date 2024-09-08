from django.urls import path
from .views import CreatePost , UpdatePost , GetPost , DeletePost 


urlpatterns = [
    path('createpost/', CreatePost.as_view()),  
    path('getpost/', GetPost.as_view()),  
    path('updatepost/', UpdatePost.as_view()),  
    path('deletepost/', DeletePost.as_view()),  
    


   
]
