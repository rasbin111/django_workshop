from django.urls import path, include

from course.models import Course
from .views import HomeView,CourseViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course', CourseViewSet, basename="course")

urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomeView.as_view()),
]
