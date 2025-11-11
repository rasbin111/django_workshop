from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.get(username=username)

        if user is not None:
            authenticated_user = authenticate(username=username, password=password)
            
            if authenticated_user:
                refresh = RefreshToken.for_user(authenticated_user)

                return Response({'message': "Logged in", "refresh": str(refresh), "access": str(refresh.access_token), "user": {
                    "id": user.id,
                    "username": user.username,
                }})
            else:
                return Response({'message': f"User with username {username} not found", }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': f"User with username {username} not found", }, status=status.HTTP_401_UNAUTHORIZED)

        