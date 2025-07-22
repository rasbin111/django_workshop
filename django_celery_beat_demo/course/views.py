from django.shortcuts import render
from celery.result import AsyncResult

from .tasks import  add, sub

def index(request):
    # print("results: ")
    # result1 = add.delay(10, 20)
    # print("result 1: ", result1)
    # result2 = sub.apply_async(args=[80, 10])
    # print("result 2: ", result2)
    result = add.delay(10, 30)
    return render(request, "course/home.html", {"result": result})

def about(request):
    print("results: ")
    return render(request, "course/about.html")

def contact(request):
    print("results: ")
    return render(request, "course/contact.html")

def check_result(request, task_id):
    result = AsyncResult(task_id)
    # print(result.ready())
    # print(result.successful())
    # print(result.failed())
    # print(result.get()) # blocks the exection of other part of program, using get directly like this
                        # removes advantage of using celery
    return render(request, "course/result.html", {"result": result})