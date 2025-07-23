from django.contrib import admin

from .models import Course, CourseEnrollment

admin.site.register([Course, CourseEnrollment])