from django.contrib import admin
from recipes.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Recipe, RecipeAdmin)
