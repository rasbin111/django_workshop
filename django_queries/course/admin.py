from django.contrib import admin

# Register your models here.
from .models import Student, Course, Creator


admin.site.register([Student, Course, Creator])