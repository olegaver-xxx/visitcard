from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Post



class IndexView(TemplateView):
    template_name = 'index.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class DetailPostView(DetailView):
    model = Post
    template_name = ...
