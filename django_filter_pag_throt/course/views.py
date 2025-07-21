from rest_framework.status import HTTP_200_OK
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from course.models import Course, CourseEnrollment
from course.serializers import CourseSerailizer, CourseEnrollmentSerializer
from course.throttling import CourseListThrottling
from course.paginations import ItemListPagination


class CourseListView(APIView):
    # permission_classes = [IsAuthenticated]
    throttle_classes = [CourseListThrottling]

    def get(self, request):
        courses = Course.objects.all()
        paginator = ItemListPagination()
        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerailizer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CourseDetailView(generics.RetrieveAPIView):
    throttle_scope = "course-detail"
    queryset = Course.objects.all()
    serializer_class = CourseSerailizer


class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer
    pagination_class = ItemListPagination