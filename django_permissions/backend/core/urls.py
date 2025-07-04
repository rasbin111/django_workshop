from django.contrib import admin
from django.urls import path, include
from account.views import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    path("admin/", admin.site.urls),
    path("user/", include("account.urls")),
    path("course/", include("course.urls")),
]
