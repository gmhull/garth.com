from django.contrib import admin
from dungeons.models import Level
# Register your models here.
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'floor_number',)
    prepopulated_fields = {'slug': ('floor_number',)}

admin.site.register(Level, LevelAdmin)
