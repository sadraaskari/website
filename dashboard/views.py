from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

def home(request):
    dash = {
        'title': 'Dashboard',
        'heading': 'Dashboard',
        'subheading': 'This is the dashboard page.',
    }
    context = {
        'dash': dash
    }
    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/podcast.html', {'title': 'About'})



