from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(template_name="projects/cover_projects.html"), name='home'),
    path('projects/', ProjectListView.as_view(template_name="projects/project_list.html"), name='project_list'),
    path('about/', views.about, name='about'),
    path('projects/<slug:slug>', ProjectDetailView.as_view(), name='project_detail')
]
