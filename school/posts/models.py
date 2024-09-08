

from django.db import models
from datetime import datetime
from authentication.models import Channel
import pytz
from datetime import datetime



class Post(models.Model):
    post_title = models.TextField(max_length = 800)
    post_likes = models.IntegerField(default= 0)
    post_comments = models.IntegerField(default= 0)
    post_time = models.DateTimeField(default=pytz.utc.localize(datetime.now()))
    channel = models.ForeignKey(Channel , on_delete=models.CASCADE,default=1 )

class PostImages(models.Model):
    post = models.ForeignKey(Post , on_delete = models.CASCADE,default=1,related_name='images')
    channel = models.ForeignKey(Channel , on_delete = models.CASCADE,default=1)
    image = models.ImageField(upload_to='post_images/%y/%m/%d')
    postimage_time = models.DateTimeField(default=pytz.utc.localize(datetime.now()))

   


