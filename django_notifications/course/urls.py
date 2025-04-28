from django.urls import path

from .views import NotificationsSendAPIView

urlpatterns = [
    path("notifications/", NotificationsSendAPIView.as_view()),
]
