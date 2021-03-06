from django.urls import path, include, re_path
from . import views
from .views import FloorDetailView
from dungeons.models import Level
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.dnd_main, name='dnd_main'),
    path('floor_<slug:slug>', FloorDetailView.as_view(), name='floor_detail')
]
