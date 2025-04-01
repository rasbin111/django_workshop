from django.db import models


class Creator(models.Model):
    name = models.CharField(max_length=100, blank=False)
    info = models.TextField()
    email = models.EmailField(blank=False)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.CharField(max_length=7)
    currency = models.CharField(max_length=10)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.title)

