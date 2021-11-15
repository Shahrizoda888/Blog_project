from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='home.html'


class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

@login_required(login_url='login')
class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']

@login_required(login_url='login')
class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']

@login_required(login_url='login')
class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
    