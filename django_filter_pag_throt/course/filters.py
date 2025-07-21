import django_filters
from course.models import CourseEnrollment


class CourseEnrollmentFilter(django_filters.FilterSet):
    paid_amount = django_filters.NumberFilter()
    paid_amount__gt = django_filters.NumberFilter(field_name="paid_amount", lookup_expr="gt")
    paid_amount__lt = django_filters.NumberFilter(field_name="paid_amount", lookup_expr="lt")

    credit_amount = django_filters.NumberFilter()
    credit_amount__gt = django_filters.NumberFilter(field_name="credit_amount", lookup_expr="gt")
    credit_amount__lt = django_filters.NumberFilter(field_name="credit_amount", lookup_expr="lt")

    class Meta:
        model = CourseEnrollment
        fields = ["paid_amount", "credit_amount"]