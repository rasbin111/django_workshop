from django.urls import re_path

from course.consumers import NotificationConsumer

websocket_urlpatterns = [
    # re_path(r"ws/notifications/(?P<user_name>\w+)/$", NotificationConsumer.as_asgi()),
    re_path(r"ws/notifications/$", NotificationConsumer.as_asgi()),
]