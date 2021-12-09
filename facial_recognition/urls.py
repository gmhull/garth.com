from django.urls import path, include, re_path
from . import views
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.face_recog, name='face_recog'),
    path('recognize', views.recognize, name='recognize_face'),
]
