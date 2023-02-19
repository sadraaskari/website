from django import forms
from .models import CounselingRequest, SendSMS, Ticket
from users.models import UserProfile
import secrets
from django.contrib.admin.widgets import FilteredSelectMultiple


class CounselingRequestForm(forms.ModelForm):
    class Meta:
        model = CounselingRequest
        fields = ('name', 'phone', 'description')

    def __init__(self, *args, **kwargs):
        super(CounselingRequestForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        counseling_request = super(CounselingRequestForm, self).save(commit=False)
        counseling_request.name = self.cleaned_data['name']
        counseling_request.phone = self.cleaned_data['phone']
        counseling_request.description = self.cleaned_data['description']
        if commit:
            counseling_request.save()
        return counseling_request


class SendSMSForm(forms.ModelForm):

    users = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = SendSMS
        fields = ('users', 'text')

    def clean(self):
        cleaned_data = super().clean()
        users = cleaned_data.get('users')
        text = cleaned_data.get('text')
        for user in users:
            SendSMS(to=user.phone, text=text).send(to=user.phone, text=text)
        return cleaned_data


class SMSPasswordResetForm(forms.Form):
    phone = forms.CharField(max_length=11, required=True)

    def send_sms(self, phone, token):
        message = 'کد بازیابی رمز عبور شما: ' + token
        SendSMS().send(to=phone, text=message)

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')

        if UserProfile.objects.filter(phone=phone).exists():
            token = secrets.token_hex(4)
            user = UserProfile.objects.get(phone=phone).user
            user.set_password(token)
            user.save()
            self.send_sms(phone=phone, token=token)
        else:
            raise forms.ValidationError('شماره موبایل وارد شده در سیستم ثبت نشده است.')
        return cleaned_data


class TicketForm(forms.ModelForm):
    receivers = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(),
                                               widget=FilteredSelectMultiple('receivers', False))

    class Meta:
        model = Ticket
        fields = ['title', 'pay_request', 'description', 'receivers', 'sender', 'sms']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TicketForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        sender = cleaned_data.get('sender')
        receivers = cleaned_data.get('receivers')
        for receiver in receivers:
            Ticket.objects.create(sender=sender, receiver=receiver, title=cleaned_data['title'],
                                  description=cleaned_data['description'], pay_request=cleaned_data['pay_request'])
            if cleaned_data['sms']:
                SendSMS().send(to=receiver.phone, text=self.cleaned_data['title'])
        return cleaned_data
