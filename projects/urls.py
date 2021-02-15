from django.urls import path, include, re_path
# from django.views.generic import ListView, DetailView
from projects.models import Project
from .views import ProjectListView, ProjectDetailView

# urlpatterns = [
#     path('', ListView.as_view(queryset=Project.objects.all().order_by("-date")[:25],template_name="projects/index.html")),
#     # I want to change this to be the project title or tag I think
#     re_path('<slug:slug>',DetailView.as_view(model=Project,template_name='projects/project.html'))
# ]

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<slug:slug>', ProjectDetailView.as_view(), name='project_detail')
]
