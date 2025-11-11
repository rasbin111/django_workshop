import json

from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_name = self.scope["url_route"]["kwargs"]["user_name"]
        self.group_name = f"{self.user_name}"

        await self.channel_layer.group_add(
            self.group_name, self.channel_name
        )
        await self.accept()

        await self.send(text_data=json.dumps({
            'type': "connection_established",
            "message": "Connected to notification system",
        }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def product_notification(self, event):
        await self.send(text_data = json.dumps({ # ws.onmessage() receives data after send() method
            "type": "product_created",
            "data": event["message"]
        }))

