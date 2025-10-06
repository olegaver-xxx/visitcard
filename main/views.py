from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Post


# Create your views here.
class MainView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
