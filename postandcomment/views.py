from django.shortcuts import render
from .models import Post, Comment


def home(request):
    posts = Post.objects.all()
    return render(request, 'postandcomment/home.html', {'posts': posts})


def about(request):
    return render(request, 'postandcomment/about.html')