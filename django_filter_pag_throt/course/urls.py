
from django.urls import path
from course.views import CourseListView, CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name="course-list"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
]
