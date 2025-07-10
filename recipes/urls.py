from django.urls import path
from . import views
from .views import RecipesListView, RecipesDetailView

urlpatterns = [
    path('', RecipesListView.as_view(template_name="personal/recipe_list.html"), name='recipe_list'),
    path('<slug:slug>', RecipesDetailView.as_view(), name='recipe_detail')
]