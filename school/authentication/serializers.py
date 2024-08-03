from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CreateChannel

class CreateChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateChannel
        fields = '__all__'
        extra_kwargs = {
            'channel_password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['channel_password'] = make_password(validated_data['channel_password'])
        return super().create(validated_data)

class SignInSerializer(serializers.Serializer):
    channel_email = serializers.EmailField()
    channel_password = serializers.CharField(write_only=True)
