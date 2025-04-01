from django.contrib import admin

# Register your models here.
from .models import Course, Creator

admin.site.register([Course, Creator])
