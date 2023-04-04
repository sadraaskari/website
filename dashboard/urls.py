from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('about/', views.about, name='dashboard-about'),
    path('ticket/', views.ticket, name='dashboard-ticket'),
    path('all_tickets/', views.all_tickets, name='dashboard-all_tickets'),
    path('card_slider/', views.card_slider, name='dashboard-card_slider'),
]
