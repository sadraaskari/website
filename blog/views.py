from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def podcast(request):
    return render(request, 'blog/podcast.html', {'title': 'podcast'})
