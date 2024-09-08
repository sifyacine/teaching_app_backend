from datetime import datetime
from django.db import models
from courses.models import Courses
# Create your models here.
class  Videos(models.Model):
    video_video = models.FileField(upload_to= 'video/%y/%m/%d')
    video_title = models.CharField(max_length=50)
    video_desc = models.CharField(max_length=800)
    video_time = models.DateTimeField(default= datetime.now())
    course = models.ForeignKey(Courses , on_delete= models.CASCADE , default= 1)

