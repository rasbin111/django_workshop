from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class NotificationsSendAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "general", {
                "type": "send_info_to_user_group",
                "text": {"status": "done"}
            }
        )
        return Response({"status": True}, status=status.HTTP_200_OK)