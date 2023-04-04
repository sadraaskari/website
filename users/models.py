from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(max_length=30, default='')
    permission = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=30, default='', unique=True)
    online_or_offline = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=4)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    student = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    major = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    school = models.CharField(max_length=30, default='')
    mother_phone = models.CharField(max_length=30, default='')
    father_phone = models.CharField(max_length=30, default='')
    home_phone = models.CharField(max_length=30, default='')
    support_id = models.IntegerField(default=0)
    counselor_id = models.IntegerField(default=0)
    manager_id = models.IntegerField(default=0)
    support_name = models.CharField(max_length=30, default='')
    counselor_name = models.CharField(max_length=30, default='')
    manager_name = models.CharField(max_length=30, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def user_id(self):
        return self.student.user.id

    def __str__(self):
        return self.student.user.username


class Exam(models.Model):
    exam_name = models.CharField(max_length=30, default='')
    exam_date = models.DateTimeField(default=timezone.now)
    exam_score = models.IntegerField(default=0)
    exam_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def student_id(self):
        return self.exam_student.student.id

    def __str__(self):
        return self.exam_name


class SumOfStudy(models.Model):
    sum_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    test_count = models.IntegerField(default=0)
    study_time = models.IntegerField(default=0)
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def student_id(self):
        return self.sum_student.student.id

    def __str__(self):
        return self.sum_student.student.user.username


