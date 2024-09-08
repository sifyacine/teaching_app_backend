from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.db import models
from authentication.models import Channel


class ShortVideo(models.Model):
    short_title = models.CharField(max_length=100)
    short_video = models.FileField(upload_to='upload/%y/%m/%d' )
    short_likes = models.IntegerField(default= 0)
    short_comments = models.IntegerField( default=0)
    short_time = models.DateTimeField(default=datetime.now())
    channel = models.ForeignKey(Channel , on_delete=models.CASCADE ,default=1)

    def increment_likes(self ):
        
         self.short_likes += 1
         self.save()
    def decrement_likes(self):
        if self.short_likes > 0:
            self.short_likes -= 1
            self.save()
        else:
            print("number the likes is 0 , so can't be decrease to -1")
    
    def increment_comments(self):
        self.short_comments += 1
        self.save()
    
    def decremnt_comments(self):
        if self.short_comments > 0:
            self.short_comments -=1
            self.save()
        else:
            print("number the comment is 0 , so can't be decrease to -1")
             


    
       


    