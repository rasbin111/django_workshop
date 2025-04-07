from django.contrib import admin

from .models import Course, Creator

admin.site.register([Course, Creator])
