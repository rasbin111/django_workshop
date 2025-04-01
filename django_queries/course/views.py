from django.db.models import Prefetch
from django.shortcuts import render
from django.http import JsonResponse
from utils.calculate_time import calculate_time

from .models import Course, Student, Creator

# Create your views here.
@calculate_time
def students_slow_query_view(request):
    courses = Course.objects.all()
    data = []
    for course in courses:
        data.append({
            "course": course.title,
            "students": [student.name for student in course.students.all()]  # Ensure you're accessing student data
        })

    return JsonResponse({
        "courses": data, 
    })


@calculate_time
def students_fast_query_view(request):
    courses = Course.objects.prefetch_related("students").all() # this line significantly improves performance
    data = []
    for course in courses:
        data.append({
            "course": course.title,
            "students": [student.name for student in course.students.all()]  # Ensure you're accessing student data
        })

    return JsonResponse({
        "courses": data, 
    })

@calculate_time
def students_faster_query_view(request):
    courses = Course.objects.prefetch_related(Prefetch("students", to_attr="students_list")).all() # this line significantly improves performance
    data = []
    for course in courses:
        data.append({
            "course": course.title,
            "students": [student.name for student in course.students_list]  # Ensure you're accessing student data
        })

    return JsonResponse({
        "courses": data, 
    })


@calculate_time
def creator_slow_query_view(request):
    courses = Course.objects.all()
    data = []
    for course in courses:
        creator = course.creator
        data.append({
            "course": course.title,
            "creator": creator.name,
        })

    return JsonResponse({
        "courses": data, 
    })


@calculate_time
def creator_fast_query_view(request):
    courses = Course.objects.select_related("creator").all() # this line significantly improves performance
    data = []
    for course in courses:
        creator = course.creator
        data.append({
            "course": course.title,
            "creator": creator.name
        })

    return JsonResponse({
        "courses": data, 
    })