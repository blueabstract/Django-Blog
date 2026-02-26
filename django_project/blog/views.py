from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

posts=[
    {
        'author':'Subarno',
        'title':'Blog Post 1',
        'content': "First post content",
        'date_posted':'February 21, 2026'
    },
    {
        'author':'Onrabus',
        'title':'Blog Post 2',
        'content': "Second post content",
        'date_posted':'February 21, 2026'
    }
]

def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

