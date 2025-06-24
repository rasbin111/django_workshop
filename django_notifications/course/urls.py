from django.urls import path

from course.views import NotifyUserView

urlpatterns = [
    path("notify/", NotifyUserView.as_view()),
]