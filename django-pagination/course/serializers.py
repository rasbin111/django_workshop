from rest_framework import serializers

from .models import Course, Creator


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = "__all__"