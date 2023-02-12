from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student


class StudentRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    father_name = forms.CharField(max_length=30, required=True)
    major = forms.ChoiceField(choices=[('math', 'math'), ('law', 'law'), ('biology', 'biology')], required=True)
    grade = forms.ChoiceField(choices=[('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], required=True)
    institute = forms.CharField(max_length=30, required=True)
    school = forms.CharField(max_length=30, required=True)
    online_or_offline = forms.ChoiceField(choices=[('online', 'online'), ('offline', 'offline')], required=True)
    student_phone = forms.IntegerField(required=True)
    mother_phone = forms.IntegerField(required=True)
    father_phone = forms.IntegerField(required=True)
    home_phone = forms.IntegerField(required=True)
    support_name = forms.ChoiceField(required=True)
    counselor_name = forms.ChoiceField(required=True)
    manager_name = forms.ChoiceField(required=True)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'father_name', 'major', 'grade', 'institute', 'school', 'online_or_offline', 'student_phone', 'mother_phone', 'father_phone', 'home_phone', 'support_name', 'counselor_name', 'manager_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(StudentRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        student_profile = Student.objects.create(student=user)
        student_profile.father_name = self.cleaned_data['father_name']
        student_profile.major = self.cleaned_data['major']
        student_profile.grade = self.cleaned_data['grade']
        student_profile.institute = self.cleaned_data['institute']
        student_profile.school = self.cleaned_data['school']
        student_profile.online_or_offline = self.cleaned_data['online_or_offline']
        student_profile.student_phone = self.cleaned_data['student_phone']
        student_profile.mother_phone = self.cleaned_data['mother_phone']
        student_profile.father_phone = self.cleaned_data['father_phone']
        student_profile.home_phone = self.cleaned_data['home_phone']
        student_profile.support_name = self.cleaned_data['support_name']
        student_profile.counselor_name = self.cleaned_data['counselor_name']
        student_profile.manager_name = self.cleaned_data['manager_name']
        if commit:
            student_profile.save()
        return user

