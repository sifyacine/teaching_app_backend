from rest_framework import serializers
from .models import Channel

class ChannelSerializer(serializers.ModelSerializer):
    channel_password = serializers.CharField(write_only=True)

    class Meta:
        model = Channel
        fields = [
            'channel_name', 'channel_email', 'channel_phone', 'channel_password',
            'channel_teacher', 'channel_img', 'channel_desc', 'channel_likes'
        ]

    def create(self, validated_data):
        password = validated_data.pop('channel_password')
        channel = Channel(**validated_data)
        channel.set_password(password)
        channel.save()
        return channel
