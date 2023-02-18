from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='users-home'),
    path('register/', views.register, name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
    path('password_reset/', views.reset_password, name='password_reset'),
    path('password_reset/done/', views.reset_password_done, name='password_reset_done'),
    path('password_change/', views.change_password, name='password_change'),
    path('password_change/done/', views.change_password_done, name='password_change_done'),
]
