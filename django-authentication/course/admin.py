from django.contrib import admin
from .models import Creator, Course

admin.site.register([Creator, Course])
