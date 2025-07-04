from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

User = get_user_model()

class HomeView(APIView):
    def get(self, request):
        print("Called")
        return Response({"data": "dashboard data"})

class LoginView(APIView):
    # Login API using email and password
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"detail": "Email and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        user = authenticate(email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.first_name,
                    },
                    "permissions": {
                        "is_superuser": user.is_superuser,
                        "is_staff": user.is_staff,
                        "is_active": user.is_active, 
                        "user_type": user.user_type,
                    },

                }
            )
            # response.set_cookie(
            #     key="access_token",
            #     value=str(refresh.access_token),
            #     httponly=True,
            #     secure=True
            # )
            # response.set_cookie(
            #     key="refresh_token",
            #     value=str(refresh),
            #     httponly=True,
            #     secure=True
            # )

            return response
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateOrUpdateUserAPIView(APIView):

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response(
                {"email": "Email is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        if not User.objects.filter(email=email).exists():
            serializer = UserSerializer(data=request.data)
        else:
            return Response(
                {"email": "Email already exist."}, status=status.HTTP_400_BAD_REQUEST
            )

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_superuser": user.is_superuser,
                    "user_type": user.user_type,
                    "is_active": user.is_active,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update user only based on id
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"id": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
