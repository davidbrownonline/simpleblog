from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create.html'
#   fields included in PostForm


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post_update.html'
