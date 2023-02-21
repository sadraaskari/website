from django.db import models
from users.models import Student
from django.utils import timezone
from users.models import UserProfile
from dashboard.models import Option
from courses.models import Tutorial


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
    merchant_id = Option.objects.get(option_key='merchant_id').option_value
    expire_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=0)
    status = 0
    description = Option.objects.get(option_key='description').option_value
    transaction_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    callback_url = Option.objects.get(option_key='callback_url').option_value
    ref_id = models.IntegerField(default=0)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, blank=True, null=True)

    def user_id(self):
        return self.transaction_user.user.id

    def __str__(self):
        return self.transaction_user.user.username
