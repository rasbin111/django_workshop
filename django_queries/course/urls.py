from django.urls import path
from .views import students_slow_query_view, students_fast_query_view, students_faster_query_view, creator_slow_query_view, creator_fast_query_view

urlpatterns = [
    path('students/slow',students_slow_query_view, ),
    path('students/fast',students_fast_query_view, ),
    path('students/faster',students_faster_query_view,),
    path('creator/slow', creator_slow_query_view),
    path('creator/fast', creator_fast_query_view)
]