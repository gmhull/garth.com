from django.contrib import admin
from projects.models import Project, ProjectPage
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

class PageInline(NestedStackedInline):
    model = ProjectPage
    fk_name = "project"
    extra = 1


class ProjectAdmin(NestedModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PageInline,]
    

admin.site.register(Project, ProjectAdmin)
