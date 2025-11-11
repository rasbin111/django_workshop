from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from product.models import Product, PurchaseProduct
from asgiref.sync import async_to_sync


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:50]}"


# @receiver(post_save, sender=Product)
# def product_created_notification(sender, instance, created, *args, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()

#         notification = Notification.objects.create(
#             # user=instance.user,
#             message = f"New product {instance.name} has been created"
#         )

#         notification_data = {
#             "type": "product_notification",
#             "message": {
#                 "id": notification.id,
#                 "user": notification.user,
#                 "message": notification.message,
#                 "created_at": notification.created_at
#             }
#         }

#         async_to_sync(channel_layer.group_send)("notifcations", notification_data)