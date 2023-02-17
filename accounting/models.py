from django.db import models
from users.models import Student
from django.utils import timezone
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
    merchant_id = "1344b5d4-0048-11e8-94db-005056a205be"
    expire_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default='')
    transaction_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    callback_url = "http://example.com/accounting/payment/status/"
    ref_id = models.IntegerField(default=0)

    def user_id(self):
        return self.transaction_user.user.id

    def __str__(self):
        return self.transaction_user.user.username







