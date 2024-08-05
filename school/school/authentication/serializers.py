from rest_framework import serializers
from .models import CreateChannel 
class CreateChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateChannel
        fields = "__all__"

