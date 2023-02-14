from django.db import models
from django.utils import timezone


class CounselingRequest(models.Model):
    name = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    access_code = models.IntegerField(default=0)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
