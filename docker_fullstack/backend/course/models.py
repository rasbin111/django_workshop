from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title