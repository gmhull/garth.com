from django.contrib import admin
from projects.models import Project, ProjectPage, Skills
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

class PageInline(NestedStackedInline):
    model = ProjectPage
    fk_name = "project"
    extra = 1


class ProjectAdmin(NestedModelAdmin):
    model = Project
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PageInline,]


class SkillsAdmin(admin.ModelAdmin):
    model = Skills
    list_display = ('name',)
    

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skills, SkillsAdmin)
