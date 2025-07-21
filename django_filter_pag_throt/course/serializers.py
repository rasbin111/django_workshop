from rest_framework import serializers
from course.models import Course, CourseEnrollment

class CourseSerailizer(serializers.ModelSerializer):
    tutor = serializers.CharField(source="tutor.username")

    class Meta:
        model = Course
        fields = "__all__"
