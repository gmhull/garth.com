from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipesListView(ListView):
    model = Recipe
    ordering = ['-date']

class RecipesDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['similar_projects'] = Project.objects.exclude(id=self.object.id).filter(type=self.object.type).order_by("-id")[:4:]
        return context
