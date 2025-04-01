# function based middleware
from sys import exception
from django.http import JsonResponse
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()

"""
def simple_middleware(get_response):
    
    # one-time configuration and initialization
    def middleware(request):
        # code be to exec for each req before the view ( and later middleware) are called
        response = get_response(request)

        # code to be executed for each request/response after the view is called 
        return response
    
    return middleware

# Equivalent to above func based middleware
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # one time configuration and initialization

    def __call__(self, request):
        # code be to exec for each req before the view ( and later middleware) are called

        response = self.get_response(request)

        # code to be executed for each request/response after the view is called 

        return response

"""


class UserInfoWithToken:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = request.path
        if "login" in login_url:
            response = self.get_response(request)
            return response
        
        token = request.headers.get("Authorization", None)
        if token:
            token = token.replace("Bearer", "").strip()
            try:
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token.get("user_id")
                user = User.objects.get(pk=user_id)
                request.email = user.email

            except jwt.ExpiredSignatureError: 
                return JsonResponse({"error": "Session expired"}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"error": "Invalid token"}, status=401)

        else:

            return JsonResponse({"error": "No token"}, status=403)

        response = self.get_response(request)
        return response
