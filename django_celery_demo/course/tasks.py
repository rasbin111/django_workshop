from course.models import Course
from django.core.cache import cache

from celery import shared_task

@shared_task()
def print_hello():
    print("Hello")

@shared_task(name="course.tasks.add")
def add(x, y):
    return x + y

@shared_task
def count_courses():
    return Course.objects.count()
