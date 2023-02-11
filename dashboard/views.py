from django.shortcuts import render

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
    return render(request, 'dashboard/about.html', {'title': 'About'})