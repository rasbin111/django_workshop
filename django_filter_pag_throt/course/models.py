from django.db import models
from django.contrib.auth.models import  User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class CourseEnrollment(models.Model):
    student_name = models.CharField(max_length=100)
    paid_amount = models.FloatField(default=0.0)
    credit_amount = models.FloatField(default=0.0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name="enrollments")

    def __str__(self):
        return str(self.student_name) + " - " + str(self.course.title)

    def save(self):
        self.credit_amount = self.course.price - self.paid_amount
        super().save()


class Account(models.Model):
    date = models.DateField(auto_now_add=True)
    totalCollectionAmount = models.PositiveIntegerField(default=0)
    totalCollectedAmount = models.PositiveBigIntegerField(default=0)
    totalCreditAmount = models.PositiveBigIntegerField(default=0)
