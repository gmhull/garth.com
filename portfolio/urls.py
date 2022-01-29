from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from . import views
from .models import Project
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(template_name="portfolio/cover_projects.html"), name='home'),
    path('projects/', ProjectListView.as_view(template_name="portfolio/project_list.html"), name='project_list'),
    path('about/', views.about, name='about'),
    path('projects/<slug:slug>', ProjectDetailView.as_view(), name='project_detail')
]
