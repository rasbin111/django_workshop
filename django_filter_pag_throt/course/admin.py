from django.contrib import admin

# Register your models here.
from .models import Course, CourseEnrollment

admin.site.register([Course, CourseEnrollment])
