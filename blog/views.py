from django.shortcuts import render

posts = [
    {
        'author': 'Momtaz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'february 10, 2023'
    },
    {
        'author': 'Momtaz',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'february 11, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.
