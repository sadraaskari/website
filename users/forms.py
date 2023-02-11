from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    father_name = forms.CharField(max_length=30, required=True)
    major = forms.CharField(max_length=30, required=True)
    grade = forms.CharField(max_length=30, required=True)
    institute = forms.CharField(max_length=30, required=True)
    school = forms.CharField(max_length=30, required=True)
    online_or_offline = forms.CharField(max_length=30, required=True)
    student_phone = forms.CharField(max_length=30, required=True)
    mother_phone = forms.CharField(max_length=30, required=True)
    father_phone = forms.CharField(max_length=30, required=True)
    home_phone = forms.CharField(max_length=30, required=True)
    support_name = forms.CharField(max_length=30, required=True)
    counselor_name = forms.CharField(max_length=30, required=True)
    manager_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'father_name', 'major', 'grade', 'institute', 'school', 'online_or_offline', 'student_phone', 'mother_phone', 'father_phone', 'home_phone', 'support_name', 'counselor_name', 'manager_name']