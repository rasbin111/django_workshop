import json 


from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.user_name = self.scope["user"]
        self.user_group_name = f"chat_{self.user_name}"
        async_to_sync(self.channel_layer.group_add)(self.user_group_name, self.channel_name)
        self.accept()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.user_group_name, self.channel_name)
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        async_to_sync(self.channel_layer.group_send)(
            self.user_group_name, {
                "type": "notifications.message",
                "message": text_data_json
            }
        )
    
    def send_info_to_user_group(self, event):
        message = event["text"]
        self.send(text_data=json.dumps(message))

    def notifications_message(self, event):
        message = event["message"]

        # Send message to websocket 
        self.send(text_data=json.dumps({"message": message}))