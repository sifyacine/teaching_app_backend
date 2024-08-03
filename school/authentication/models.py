from django.db import models
from datetime import datetime
import random 
# Create your models here.
class CreateChannel(models.Model):
    channel_name =models.CharField(max_length= 15, default="Unknown")
    channel_email = models.EmailField(max_length = 254)
    channel_password = models.CharField(max_length=254)
    channel_phone = models.CharField(max_length=10)
    channel_desc = models.TextField(max_length=275)
    channel_img = models.CharField(max_length=20)
    channel_likes = models.IntegerField()
    channel_type = models.CharField(max_length=11)
    channel_verifycode = models.CharField(max_length=6)
    channel_approve = models.BooleanField(default=False)
    
    
    
