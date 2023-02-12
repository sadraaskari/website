from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(max_length=30, default='')
    id = models.AutoField(primary_key=True, default=1)

    def __str__(self):
        return self.role


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default=0)
    online_or_offline = models.CharField(max_length=30, default='')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30, default='')
    major = models.CharField(max_length=30, default='')
    grade = models.CharField(max_length=30, default='')
    institute = models.CharField(max_length=30, default='')
    school = models.CharField(max_length=30, default='')
    online_or_offline = models.CharField(max_length=30, default='')
    student_phone = models.CharField(max_length=30, default='')
    mother_phone = models.CharField(max_length=30, default='')
    father_phone = models.CharField(max_length=30, default='')
    home_phone = models.CharField(max_length=30, default='')
    support_name = models.CharField(max_length=30, default='')
    counselor_name = models.CharField(max_length=30, default='')
    manager_name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.student.username
