import subprocess
from django.forms import ValidationError
from rest_framework import serializers
from .models import ShortVideo
import mimetypes
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
import subprocess
from .models import ShortVideo

def validate_file_size(value: UploadedFile):
    """
    يتحقق من حجم الملف، ويسمح بحد أقصى 100 ميجابايت.
    """
    max_size = 104857600  # 100 ميجابايت بالبايت
    if value.size > max_size:
        raise ValidationError("حجم الملف كبير جدًا. الحد الأقصى المسموح به هو 100 ميجابايت.")
    return value

def validate_file_extension(value: UploadedFile):
    """
    يتحقق من امتداد الملف، ويسمح فقط بملفات MP4.
    """
    allowed_extensions = ['mp4']
    ext = value.name.split('.')[-1].lower()
    mime_type, _ = mimetypes.guess_type(value.name)

    if ext not in allowed_extensions or not mime_type.startswith('video/'):
        raise ValidationError("يُسمح فقط بملفات MP4 صالحة. يرجى اختيار ملف فيديو MP4.")
    return value


# Create your models here.
class ShortVideoSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = ShortVideo
        fields = ['short_title', 'short_video', 'short_likes', 'short_comments', 'short_time', 'channel']

    short_video = serializers.FileField(validators=[validate_file_size, validate_file_extension ])
        

    
class LikeAndCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()


