from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, UserProfile, Role
from dashboard.models import SendSMS
import secrets
import re


def get_support_names():
    support_names = []
    for support in UserProfile.objects.filter(role__role='support'):
        support_names.append((support.user_id, support.user.username))
    return support_names


def get_counselor_names():
    counselor_names = []
    for counselor in UserProfile.objects.filter(role__role='counselor'):
        counselor_names.append((counselor.user_id, counselor.user.username))
    return counselor_names


def get_manager_names():
    manager_names = []
    for manager in UserProfile.objects.filter(role__role='manager'):
        manager_names.append((manager.user_id, manager.user.username))
    return manager_names


class ValidationCodeForm(forms.Form):
    validation_code = forms.CharField(max_length=8, required=True)
    verifier = 0

    def clean_validation_code(self):
        code = self.cleaned_data['validation_code']
        if code != self.verifier:
            raise forms.ValidationError('کد تایید صحیح نیست')
        return code


class BasicRegistration(UserCreationForm):
    phone = forms.IntegerField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    father_name = forms.CharField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()

    code = secrets.token_hex(4)

    def send_sms(self):
        phone = self.cleaned_data['phone']
        phone_number = str(phone)
        if UserProfile.objects.filter(phone=phone).exists():
            raise forms.ValidationError('شماره تلفن وارد شده قبلا ثبت شده است')
        elif not re.match(r'^9\d{9}$', str(phone_number)):
            raise forms.ValidationError('شماره تلفن وارد شده صحیح نیست')
        else:
            ValidationCodeForm.verifier = self.code
            text = 'کد تایید شما: ' + self.code
            SendSMS().send(to=phone, text=text)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['phone']
        user.set_password(self.code)
        if commit:
            user.save()
            userprofile = UserProfile.objects.create(user=user)
            userprofile.father_name = self.cleaned_data['father_name']
            userprofile.phone = self.cleaned_data['phone']
            if commit:
                userprofile.save()
        return user


class UserRegisterForm(forms.Form):
    online_or_offline = forms.ChoiceField(choices=[('1', 'online'), ('0', 'offline')], required=True)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)
    institute = forms.CharField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    class Meta:
        fields = ['online_or_offline', 'role', 'institute']

    def save(self, commit=True):
        user = self.user
        userprofile = UserProfile.objects.get(user=user)
        userprofile.online_or_offline = self.cleaned_data['online_or_offline']
        userprofile.role = self.cleaned_data['role']
        userprofile.institute = self.cleaned_data['institute']
        if commit:
            userprofile.save()
        return userprofile


class StudentRegisterForm(forms.Form):
    major = forms.ChoiceField(choices=[('1', 'math'), ('2', 'law'), ('3', 'biology')], required=True)
    grade = forms.ChoiceField(choices=[('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], required=True)
    institute = forms.CharField(max_length=30, required=True)
    school = forms.CharField(max_length=30, required=True)
    student_phone = forms.IntegerField(required=True)
    mother_phone = forms.IntegerField(required=True)
    father_phone = forms.IntegerField(required=True)
    home_phone = forms.IntegerField(required=True)
    support_name = forms.ChoiceField(choices=get_support_names(), required=True)
    counselor_name = forms.ChoiceField(choices=get_counselor_names(), required=True)
    manager_name = forms.ChoiceField(choices=get_manager_names(), required=True)

    class Meta:
        fields = ['major', 'grade', 'institute', 'school', 'mother_phone', 'father_phone', 'home_phone', 'support_name', 'counselor_name', 'manager_name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = self.user
        userprofile = UserProfile.objects.get(user=user)
        student = Student.objects.create(student=userprofile)
        student.major = self.cleaned_data['major']
        student.grade = self.cleaned_data['grade']
        student.institute = self.cleaned_data['institute']
        student.school = self.cleaned_data['school']
        student.mother_phone = self.cleaned_data['mother_phone']
        student.father_phone = self.cleaned_data['father_phone']
        student.home_phone = self.cleaned_data['home_phone']
        student.support_id = self.cleaned_data['support_name']
        student.counselor_id = self.cleaned_data['counselor_name']
        student.manager_id = self.cleaned_data['manager_name']
        support = UserProfile.objects.get(user_id=student.support_id)
        student.support_name = support.user.username
        counselor = UserProfile.objects.get(user_id=student.counselor_id)
        student.counselor_name = counselor.user.username
        manager = UserProfile.objects.get(user_id=student.manager_id)
        student.manager_name = manager.user.username

        if commit:
            student.save()
        return user

