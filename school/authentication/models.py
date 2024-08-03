from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class CreateChannel(models.Model):
    channel_name = models.CharField(max_length=15, default="Unknown", validators=[MinLengthValidator(3)])
    channel_email = models.EmailField(max_length=254, unique=True)
    channel_password = models.CharField(max_length=254)
    channel_phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message='Phone number must be 10 digits')])
    channel_desc = models.TextField(max_length=275, blank=True)
    channel_img = models.CharField(max_length=20, blank=True)
    channel_likes = models.IntegerField(default=0)
    channel_teacher = models.BooleanField(default=False)
    channel_verifycode = models.CharField(max_length=6, blank=True)
    channel_approve = models.BooleanField(default=False)

    def __str__(self):
        return self.channel_name
