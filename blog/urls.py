from django.urls import path 
from .views import (
    BlogDetailView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)
urlpatterns = [
    path('post/<int:pk>/delete/',BlogDeleteView,name='post_delete'),
    path('post/<int:pk>/edit/',BlogUpdateView,name='post_edit'),
    path('',BlogListView,name='home'),
    path('post/<int:pk>/',BlogDetailView,name='post_detail'),
    path('post/new/',BlogCreateView, name='post_new'),


]
