from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator, RegexValidator

class ChannelManager(BaseUserManager):
    def create_user(self, channel_email, channel_password=None, **extra_fields):
        if not channel_email:
            raise ValueError("Channels must have an email address")
                
        channel_email=self.normalize_email(channel_email),
        user = self.model(email = channel_email, **extra_fields)
        user.set_password(channel_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, channel_email, channel_password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(channel_email, channel_password, **extra_fields)

class Channel(AbstractBaseUser):
    channel_name = models.CharField(max_length=150, default="Unknown", validators=[MinLengthValidator(3)])
    channel_email = models.EmailField(max_length=254, unique=True)
    channel_phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message='Phone number must be 10 digits')])
    channel_desc = models.TextField(max_length=275, blank=True)
    channel_img = models.CharField(max_length=20, blank=True)
    channel_likes = models.IntegerField(default=0)
    channel_teacher = models.BooleanField(default=False)
    channel_verifycode = models.CharField(max_length=6, blank=True)
    channel_approve = models.BooleanField(default=False)

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = ChannelManager()

    USERNAME_FIELD = 'channel_email'
    REQUIRED_FIELDS = ['channel_name', 'channel_phone']

    def __str__(self):
        return self.channel_email