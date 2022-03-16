from django.urls import path, include, re_path
from . import views
from .views import FloorDetailView
from dungeons.models import Level
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.dnd_main, name='dnd_main'),
    path('map', views.map, name='map'),
    path('gauntlet', views.gauntlet, name='gauntlet'),
    path('level_<int:level>', views.show_level, name='level'),
    path('end', views.end, name='gauntlet_end'),
    path('no_access', views.no_access, name='no_access'),
    path('not_found', views.no_access, name='not_found'),
    path('enterance', views.enterance, name='enterance'),
]
