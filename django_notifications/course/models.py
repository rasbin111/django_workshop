from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    language = models.CharField(max_length=20, default="English", blank=True)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=10)


    def __str__(self):
        return str(self.title)