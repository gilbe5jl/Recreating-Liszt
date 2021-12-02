from django.shortcuts import render
from .models import Post

#when adding new pages or tabs up top, make new def for whatever you want
#make sure the home/blank.html is the correct route

def home(request):
    context = {

    'posts': Post.objects.all()

    }
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', {'title': 'About'})


def AI(request):
    return render(request, 'home/AI.html', {'title': 'Source Code'})

def liszt(request):
    return render(request, 'home/liszt.html', {'title': 'Who is Franz Liszt?'})

def project(request):
    return render(request, 'home/project.html', {'title': 'Our Project'})

def music(request):
    return render(request, 'home/music.html', {'title': 'Music'})





