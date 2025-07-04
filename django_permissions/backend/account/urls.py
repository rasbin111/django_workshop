from django.urls import path
from .views import CreateOrUpdateUserAPIView, LoginView, UserListAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", LoginView.as_view(), name="user-login"),
    path("create/", CreateOrUpdateUserAPIView.as_view(), name="user-create"),
    path("update/<int:pk>", CreateOrUpdateUserAPIView.as_view(), name="user-update"),
    path("list/", UserListAPIView.as_view(), name="user-list"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token-refresh'),
]
