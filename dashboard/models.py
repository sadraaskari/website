from django.db import models
from django.utils import timezone
from users.models import UserProfile
from melipayamak import Api


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


class Ticket(models.Model):
    title = models.CharField(max_length=30, default='')
    pay_request = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,null=True, related_name='receiver')
    sms = models.BooleanField(default=False)

    def sender_id(self):
        return self.sender.user.id

    def receiver_id(self):
        return self.receiver.user.id

    def __str__(self):
        return self.title


class Option(models.Model):
    option_key = models.CharField(max_length=30, default='')
    option_value = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.option_key


class SendSMS(models.Model):

    to = models.CharField(max_length=100, default='')
    text = models.CharField(max_length=100, default='')

    def send(self, to, text):
        username = Option.objects.get(option_key='username').option_value
        password = Option.objects.get(option_key='password').option_value
        sender = Option.objects.get(option_key='sender_number').option_value
        api = Api(username, password)
        sms = api.sms()
        response = sms.send(to=to, _from=sender, text=text)
        return response


