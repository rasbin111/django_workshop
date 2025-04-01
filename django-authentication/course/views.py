from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import  Response
from rest_framework.permissions import AllowAny

from course.models import Course
from .serializers import CourseSerializer 


class HomeView(APIView):

    # permission_classes = [AllowAny]
    def get(self, request):
        content = {
            'message': 'Hello world',
            
        }
        if request.email:
            content["email"] = request.email
        return Response(content)

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()  
    serializer_class = CourseSerializer
