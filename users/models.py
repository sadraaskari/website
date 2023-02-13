from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(max_length=30, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default=0)
    online_or_offline = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    student = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    major = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    institute = models.CharField(max_length=30, default='')
    school = models.CharField(max_length=30, default='')
    mother_phone = models.IntegerField(default=0)
    father_phone = models.IntegerField(default=0)
    home_phone = models.IntegerField(default=0)
    support_id = models.IntegerField(default=0)
    counselor_id = models.IntegerField(default=0)
    manager_id = models.IntegerField(default=0)
    support_name = models.CharField(max_length=30, default='')
    counselor_name = models.CharField(max_length=30, default='')
    manager_name = models.CharField(max_length=30, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student.user.username


