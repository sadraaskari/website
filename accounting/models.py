from django.db import models
from users.models import Student
from django.utils import timezone
from courses.models import Tutorial
from users.models import UserProfile


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    installment = models.JSONField(default=dict)

    def student_id(self):
        return self.student.student.id

    def __str__(self):
        return self.student.student.user.username


class Division(models.Model):
    division_type = models.IntegerField(default=0)
    division_value = models.JSONField(default=dict)
    created_at = models.DateTimeField(default=timezone.now)


class Transaction(models.Model):
    expire_date = models.DateTimeField(default=timezone.now)
    transaction_value = models.IntegerField(default=0)
    transaction_code = models.IntegerField(default=0)
    transaction_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def user_id(self):
        return self.transaction_user.user.id

    def __str__(self):
        return self.transaction_user.user.username







