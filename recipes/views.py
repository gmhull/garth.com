from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    ordering = ['-date']


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
