from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CourseViewset, CreatorViewset

router = DefaultRouter()

router.register("course", CourseViewset, basename="course")
router.register("creator", CreatorViewset, basename="creator")

urlpatterns = [
    path("", include(router.urls)),
]