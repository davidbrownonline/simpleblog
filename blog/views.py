from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/update_post.html'
    