from rest_framework import serializers
from .models import Group, GroupMembership, Message, File, Image, Link
from authentication.serializers import ChannelSerializer



class GroupMembershipSerializer(serializers.ModelSerializer):
    user = ChannelSerializer(read_only=True)  # Use the full ChannelSerializer to provide detailed user information

    class Meta:
        model = GroupMembership
        fields = ['id', 'user', 'group', 'joined_at', 'approved']

class GroupSerializer(serializers.ModelSerializer):
    admin = ChannelSerializer(read_only=True)  # Include the admin details as a nested serializer
    members = GroupMembershipSerializer(source='groupmembership_set', many=True, read_only=True)  # Include the group members

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'is_private', 'admin', 'members', 'image']

    def create(self, validated_data):
        request = self.context.get('request')
        if request is None:
            raise ValueError("Request context is missing.")
        user = request.user
        validated_data['admin'] = user
        return super().create(validated_data)

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.channel_name')

    class Meta:
        model = Message
        fields = ['id', 'group', 'sender', 'content', 'sent_at']

class FileSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.channel_name')

    class Meta:
        model = File
        fields = ['id', 'group', 'sender', 'file', 'sent_at']

class ImageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.channel_name')

    class Meta:
        model = Image
        fields = ['id', 'group', 'sender', 'image', 'sent_at']

class LinkSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.channel_name')

    class Meta:
        model = Link
        fields = ['id', 'group', 'sender', 'url', 'sent_at']