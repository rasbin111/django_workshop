from django.urls import path

from .views import db_check_view
urlpatterns = [
    path("db_check/", db_check_view, ),
]
