from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, ProjectPage

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
    template_name = "projects/project_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = ProjectPage.objects.filter(project=self.object)
        return context

