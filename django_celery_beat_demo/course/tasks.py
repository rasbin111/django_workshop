from course.models import Course
from celery import shared_task
import openpyxl
import os


@shared_task
def calculateCollectedAmount():
    courses = Course.objects.all()
    courses_collection = {}
    for course in courses:
        total = 0
        for enrollment in course.enrollments.all():
            total += enrollment.paid_amount
        courses_collection[course.id] = total
    print(courses_collection)
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "sheets", "account_records.xlsx")
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    max_row = sheet.max_row
    for idx, (key, value) in enumerate(courses_collection.items()):
        sheet.append((idx+max_row, key, value))

    wb.save(filename="sheets/account_records.xlsx")


@shared_task
def calculateCreditAmount():
    courses = Course.objects.all()
    courses_credit = {}
    for course in courses:
        total = 0
        for enrollment in course.enrollments.all():
            total += enrollment.credit_amount
        courses_credit[course.id] = total
    return courses_credit

