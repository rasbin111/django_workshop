from django.urls import path, include

from rest_framework.routers import DefaultRouter


from .views import PostViewset

router = DefaultRouter()

router.register(r"posts", PostViewset, basename='post')

urlpatterns = [
    path("", include(router.urls)),
]