from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .models import Course, Creator
from .serializers import CourseSerializer, CreatorSerializer
from .utils import Custompagination, CursorCustomPagination

class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    pagination_class = CursorCustomPagination

class CreatorViewset(ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    pagination_class = Custompagination