from django.urls import path, include, re_path
from . import views
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.dnd_main, name='dnd_main')
]
