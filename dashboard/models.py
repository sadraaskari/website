from django.db import models
from django.utils import timezone
from users.models import UserProfile


class CounselingRequest(models.Model):
    name = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    access_code = models.IntegerField(default=0)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.title


class Message(models.Model):
    title = models.CharField(max_length=30, default='')
    pay_request = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')

    def sender_id(self):
        return self.sender.user.id

    def receiver_id(self):
        return self.receiver.user.id

    def __str__(self):
        return self.title
