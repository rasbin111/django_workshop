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
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name="course", blank=False)

    def __str__(self):
        return str(self.title)


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.name
