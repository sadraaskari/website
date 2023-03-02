from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegisterForm, BasicRegistration, ValidationCodeForm, UserRegisterForm
from dashboard.forms import SMSPasswordResetForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User


def home(request):
    return render(request, 'users/home.html')


def basic_registration(request):
    if request.method == 'POST':
        form = BasicRegistration(request.POST)
        if form.is_valid():
            form.send_sms()
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('users-register_validation_code')
    else:
        form = BasicRegistration()
    return render(request, 'users/register_validation.html', {'form': form})


def register_validation_code(request):
    if request.method == 'POST':
        form = ValidationCodeForm(request.POST)
        if form.is_valid():
            return redirect('users-register')
    else:
        form = ValidationCodeForm()
    return render(request, 'users/register_validation_code.html', {'form': form})


def register(request):
    user = None
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        form = UserRegisterForm(request.POST, user=user)
        if form.is_valid():
            messages.success(request, f'Account created for {form.cleaned_data.get("username")}!')
            form.save()
            if user.userprofile.role_id == 4:
                return redirect('users-student_register')
            return redirect('users-login')
    else:
        form = UserRegisterForm(request.POST, user=user)
    return render(request, 'users/register.html', {'form': form})


def student_register(request):
    user = None
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        form = StudentRegisterForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = StudentRegisterForm(request.POST, user=user)
    return render(request, 'users/student_register.html', {'form': form})


def reset_password(request):
    form = SMSPasswordResetForm()
    if request.method == 'POST':
        form = SMSPasswordResetForm(request.POST)
        if form.is_valid():
            return redirect('password_reset_done')
    return render(request, 'users/reset_password.html', {'form': form})


def reset_password_done(request):
    return render(request, 'users/reset_password_done.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def change_password(request):
    return auth_views.PasswordChangeView.as_view(template_name='users/password_change.html')(request)


@login_required
def change_password_done(request):
    return auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html')(request)
