from django.db import models
from users.models import UserProfile
from django.utils import timezone


class Tutorial(models.Model):
    tutorial_name = models.CharField(max_length=40, default='')
    tutorial_creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tutorial_type = models.IntegerField(default=0)
    tutorial_price = models.IntegerField(default=0)
    tutorial_discount = models.IntegerField(default=0)
    tutorial_image = models.ImageField(upload_to='tutorial_images', blank=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def creator_id(self):
        return self.tutorial_creator.user.id

    def __str__(self):
        return self.tutorial_name


