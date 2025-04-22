from django.urls import path
from .views import log_view

urlpatterns = [
    path("log_view", log_view),
]
