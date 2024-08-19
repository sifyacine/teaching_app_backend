import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from .models import Group, Message

User = get_user_model()

class ChatroomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.group_name = f'chat_{self.group_id}'

        # Join the group channel
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group channel
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']

        # Save the message in the database
        group = await self.get_group(self.group_id)
        await self.save_message(user, group, message)

        # Send the message to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username  # Changed from channel_name to username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))

    @database_sync_to_async
    def get_group(self, group_id):
        return Group.objects.get(id=group_id)

    @database_sync_to_async
    def save_message(self, user, group, message):
        return Message.objects.create(sender=user, group=group, content=message)



class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            # Join a room specific to the user for online status
            self.room_name = f'online_{self.user.id}'
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name
            )
            await self.accept()

            # Broadcast to the group that the user is online
            await self.channel_layer.group_send(
                'online_status',
                {
                    'type': 'user_online',
                    'user_id': self.user.id
                }
            )

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            # Leave the room specific to the user
            await self.channel_layer.group_discard(
                self.room_name,
                self.channel_name
            )

            # Broadcast to the group that the user is offline
            await self.channel_layer.group_send(
                'online_status',
                {
                    'type': 'user_offline',
                    'user_id': self.user.id
                }
            )

    async def user_online(self, event):
        # Handle when a user comes online
        await self.send(text_data=json.dumps({
            'status': 'online',
            'user_id': event['user_id']
        }))

    async def user_offline(self, event):
        # Handle when a user goes offline
        await self.send(text_data=json.dumps({
            'status': 'offline',
            'user_id': event['user_id']
        }))
