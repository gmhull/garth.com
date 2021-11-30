from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from . import views
from projects.models import Project

urlpatterns = [
    path('', ListView.as_view(queryset=Project.objects.all().order_by("-date")[:25],template_name="projects/cover_projects.html"), name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # path('trythis/', views.trythis, name='trythis'),
]
