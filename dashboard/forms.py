from django import forms
from .models import CounselingRequest, SendSMS
from users.models import UserProfile


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
