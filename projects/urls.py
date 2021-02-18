from django.urls import path, include, re_path
# from django.views.generic import ListView, DetailView
from projects.models import Project
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<slug:slug>', ProjectDetailView.as_view(), name='project_detail')
]
