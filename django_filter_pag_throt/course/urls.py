
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import CourseListView, CourseDetailView, CourseEnrollmentViewSet

router = DefaultRouter()
router.register(r"course-enrollment", CourseEnrollmentViewSet, basename="course-enrollment")

urlpatterns = [
    path("", include(router.urls)),
    path('list/', CourseListView.as_view(), name="course-list"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
]
