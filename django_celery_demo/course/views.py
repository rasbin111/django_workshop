from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .tasks import add, count_courses


def course_home(request):
    result = add.delay(20, 30)

    return HttpResponse(f"Task ID: {result.id}")


def check_task_status(request, task_id):
    result = AsyncResult(task_id)

    if result.ready():
        return HttpResponse(f"Task Result: {result.result}")
    else:
        return HttpResponse(f"Task is still running")

def run_periodic_tasks(request):
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )

    periodic_task, _ = PeriodicTask.objects.get_or_create(
        name="Count Courses",
        task="course.tasks.count_courses",
        interval=schedule,
    )

    return HttpResponse("Periodic Task Created")    
      