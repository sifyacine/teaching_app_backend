from rest_framework import serializers

from authentication.serializers import ChannelSerializer
from .models import Post , PostImages 
import mimetypes
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from postlike.serializers import PostLikeSerializer


def validate_image_size(value: UploadedFile):
    limit_mb = 2
    print(f"Image size: {value.size} bytes, limit: {limit_mb * 1024 * 1024} bytes")  # إضافة سطر للطباعة
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"حجم الصورة يجب ألا يتجاوز {limit_mb} ميجابايت.")
    return value


def validate_image_extension(value: UploadedFile):
    """
    تحقق من صحة لاحقة صورة.

    :param value: ملف الصورة المرفوع.
    :return: لا تعيد أي قيمة إذا كانت الصورة صالحة، وترفع استثناء ValidationError إذا كانت غير صالحة.
    """

    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
    # الحصول على اللاحقة من اسم الملف وتوحيد الحروف إلى حروف صغيرة
    ext = value.name.split('.')[-1].lower()

    # التحقق من اللاحقة باستخدام قائمة الامتدادات المسموح بها
    if ext not in allowed_extensions:
        raise ValidationError("يُسمح فقط بملفات الصور (jpg, jpeg, png, gif)")

    # التحقق من نوع MIME باستخدام مكتبة mimetypes
    mime_type, _ = mimetypes.guess_type(value.name)
    if not mime_type.startswith('image/'):
        raise ValidationError("الملف المرفوع ليس صورة")

    return value
class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['post','channel','image','postimage_time']
    image = serializers.ImageField(validators=[validate_image_extension , validate_image_size])
        
class PostsSerializer(serializers.ModelSerializer):
    images = PostImagesSerializer(many = True , read_only = True)
    likes = PostLikeSerializer(many = True,read_only = True)
    comments = PostLikeSerializer(many = True,read_only = True)
    channel = ChannelSerializer(required=False)

    class Meta:
        model = Post
        fields = ['post_title','post_likes','post_comments','post_time','channel','images','likes','comments']
    


    
    

    
