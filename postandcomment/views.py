from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'postandcomment/home.html', {'posts': posts})

class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'postandcomment/home.html'
    ordering = ['-date_created']

class DetailPageView(DetailView):
    model = Post

class CreatePageView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePageView(
     LoginRequiredMixin,
        UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # for the original user to update their posts themselves
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class DeletePageView(LoginRequiredMixin,
                         UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'postandcomment/about.html')