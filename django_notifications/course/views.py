from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class NotifyUserView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get("message", "Default message")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "user",
            {
            "type": "send.notifications",
            "message": message
        })
        return Response({"status": "Notification sent"})