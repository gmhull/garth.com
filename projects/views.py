from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.
def about(request):
    return render(request, 'projects/about.html')

def projects(request):
    return render(request, 'projects/projects.html')

class ProjectListView(ListView):
    model = Project
    ordering = ['-date']

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/test.html"
    # template_name = "projects/project_detail.html"

    # def __init__(self, *args, **kwargs):
    #     super(DetailView, self).__init__(*args, **kwargs)
    #
    #     print(self.model.type)
