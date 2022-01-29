from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.
def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

class ProjectListView(ListView):
    model = Project
    ordering = ['-date']

class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
