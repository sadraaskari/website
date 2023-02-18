from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegisterForm
from dashboard.forms import SMSPasswordResetForm
from django.contrib.auth import views as auth_views


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Account created for {form.cleaned_data.get("username")}!')
            form.save()
            return redirect('users-login')

    else:
        form = StudentRegisterForm()
    return render(request, 'users/register.html', {'form': form})


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
