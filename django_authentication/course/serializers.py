from rest_framework.serializers import ModelSerializer

from .models import Course, Creator 


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

class CreatorSerializer(ModelSerializer):

    class Meta:
        model = Creator
        fields = "__all__"

