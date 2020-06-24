from django.shortcuts import render
from .models import Post, Comment


def home(request):
    post = Post.objects.all()
    return render(request, 'postandcomment/home.html', {'post': post})

