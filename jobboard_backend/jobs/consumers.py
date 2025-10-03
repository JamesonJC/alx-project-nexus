# jobs/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class JobUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'job_updates'  # can dynamically be changed based on job ID or category
        self.room_group_name = f"job_{self.room_name}"

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'job_message',
                'message': message
            }
        )

    # Receive message from room group
    async def job_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
