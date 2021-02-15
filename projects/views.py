from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = "projects/index.html"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project.html"
