from rest_framework.status import HTTP_200_OK
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from course.serializers import CourseSerailizer
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .throttling import CourseListThrottling


class CourseListView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [CourseListThrottling]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerailizer(courses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CourseDetailView(RetrieveAPIView):
    throttle_scope = "course-detail"
    queryset = Course.objects.all()
    serializer_class = CourseSerailizer
