from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.

class LoginView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")


        if not email:
            return JsonResponse({"error": "email required"})

        elif not password:
            return JsonResponse({"error": "password required"})

        user = authenticate(email=email, password=password)

        if user:
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            return JsonResponse({"access": str(access_token)})
        else:
            return JsonResponse({"error": "Not valid user"})
            

