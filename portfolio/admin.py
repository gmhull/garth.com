from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
