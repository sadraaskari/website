from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounting-home'),
    path('make_payment/<int:pk>/', views.make_payment, name='make_payment'),
    path('payment/status/<int:pk>/',views.payment_status, name='payment_status'),
]