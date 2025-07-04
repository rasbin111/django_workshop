from rest_framework import serializers


from .models import Course, CourseEnrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

    def validate(self, data):
        # Ensure that a user cannot enroll in the same course multiple times
        if CourseEnrollment.objects.filter(user=data['user'], course=data['course']).exists():
            raise serializers.ValidationError("You are already enrolled in this course.")
        return data