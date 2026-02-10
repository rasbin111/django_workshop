from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.gis.geoip2 import GeoIP2

User = get_user_model()


class UserLoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(email=email, password=password)
        
        
        if user:
            x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
            
            if x_forwarded_for:

                ip = x_forwarded_for.split(",")[0].strip()
            else:
                ip = request.META.get("REMOTE_ADDR")
            
            geo = GeoIP2()
            try:
                city = geo.city(ip)
                return Response({"message": "Logged in", "ip": ip, "country": city["country_name"], "city": city["city"]})
            except Exception as e:
                return Response({"message": "Logged in", "ip": "Info not found", "ip_err": str(e)})
        else:
            return Response({"message": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
