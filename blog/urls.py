from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('podcast/', views.podcast, name='blog-podcast'),
]
