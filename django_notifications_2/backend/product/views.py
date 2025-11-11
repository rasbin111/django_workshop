from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product, PurchaseProduct
from notification.models import Notification
from .serializers import ProductSerializer

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        notification = Notification.objects.create(
            user=request.user,
            message=f"New product {product.name} has been created"
        )

        notification_data = {
            "type": "product_notification",   # method to be called in consumers.py
            "message": {
                "id": notification.id,
                "user": request.user.username,  
                "message": notification.message,
                "created_at": str(notification.created_at)
            }
        }

        channel_layer = get_channel_layer()
        room_name = request.user.username  

        async_to_sync(channel_layer.group_send)(
            f"{room_name}",     
            notification_data
        )

        return super().create(request, *args, **kwargs)