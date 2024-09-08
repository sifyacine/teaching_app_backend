from django.db import models
from posts.models import Post
from authentication.models import Channel
from datetime import datetime
# Create your models here.
class PostLike(models.Model):
    post = models.ForeignKey(Post ,  on_delete=models.CASCADE,default=1 , related_name='likes')
    channel = models.ForeignKey(Channel , on_delete=models.CASCADE,default=1)
    postlike_time = models.DateTimeField(default=datetime.now())
    