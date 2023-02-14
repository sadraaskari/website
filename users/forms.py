from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from .models import UserProfile
from .models import Role


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




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.IntegerField(required=True)
    online_or_offline = forms.ChoiceField(choices=[('1', 'online'), ('0', 'offline')], required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'online_or_offline', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        userprofile = UserProfile.objects.create(user=user)
        userprofile.father_name = self.cleaned_data['father_name']
        userprofile.phone = self.cleaned_data['student_phone']
        userprofile.online_or_offline = self.cleaned_data['online_or_offline']
        if commit:
            userprofile.save()









class StudentRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    father_name = forms.CharField(max_length=30, required=True)
    major = forms.ChoiceField(choices=[('1', 'math'), ('2', 'law'), ('3', 'biology')], required=True)
    grade = forms.ChoiceField(choices=[('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], required=True)
    institute = forms.CharField(max_length=30, required=True)
    school = forms.CharField(max_length=30, required=True)
    online_or_offline = forms.ChoiceField(choices=[('1', 'online'), ('0', 'offline')], required=True)
    student_phone = forms.IntegerField(required=True)
    mother_phone = forms.IntegerField(required=True)
    father_phone = forms.IntegerField(required=True)
    home_phone = forms.IntegerField(required=True)
    support_name = forms.ChoiceField(choices=get_support_names(), required=True)
    counselor_name = forms.ChoiceField(choices=get_counselor_names(), required=True)
    manager_name = forms.ChoiceField(choices=get_manager_names(), required=True)
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

        userprofile = UserProfile.objects.create(user=user, role=Role.objects.get(role='student'))
        userprofile.father_name = self.cleaned_data['father_name']
        userprofile.phone = self.cleaned_data['student_phone']
        userprofile.online_or_offline = self.cleaned_data['online_or_offline']
        if commit:
            userprofile.save()

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

