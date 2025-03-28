from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'

