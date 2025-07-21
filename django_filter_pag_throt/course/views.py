from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.status import HTTP_200_OK
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from course.models import Course, CourseEnrollment
from course.serializers import CourseSerailizer, CourseEnrollmentSerializer
from course.throttling import CourseListThrottling
from course.paginations import ItemListPagination
from course.filters import CourseEnrollmentFilter


class CourseListView(APIView):
    # filter_class can't be used on APIView
    permission_classes = [IsAuthenticated]
    throttle_classes = [CourseListThrottling]

    def get(self, request):
        queryset = self.get_queryset()
        paginator = ItemListPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CourseSerailizer(result_page, many=True)
        response = paginator.get_paginated_response(serializer.data)
        response.status_code = HTTP_200_OK
        return response

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(tutor=user)


class CourseDetailView(generics.RetrieveAPIView):
    throttle_scope = "course-detail"
    queryset = Course.objects.all()
    serializer_class = CourseSerailizer


class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer
    pagination_class = ItemListPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CourseEnrollmentFilter
    filterset_fields = ["paid_amount"]
    search_fields = ["student_name", "course__title"]
    ordering_fields = ["course__title", "credit_amount", "paid_amount"]
