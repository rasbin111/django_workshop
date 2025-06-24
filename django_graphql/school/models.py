from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
