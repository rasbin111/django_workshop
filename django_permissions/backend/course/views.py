from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAuthenticated

from .serializers import CourseSerializer, CourseEnrollmentSerializer
from .models import Course, CourseEnrollment


# Create your views here.
class CourseView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Course.objects.all()

    def get(self, request):
        courses = Course.objects.all()
        self.check_object_permissions(request, courses)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        course = Course(request.data)
        serializer = CourseSerializer(course)
        if serializer.is_valid():
            course.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
