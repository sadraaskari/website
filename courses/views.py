from django.shortcuts import render
from .models import Tutorial

def home(request):
    context = {
        'tutorials': Tutorial.objects.all()
    }

    return render(request, 'courses/home.html', context)
