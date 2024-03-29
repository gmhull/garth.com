"""
From the django documentation for extending the existing user model.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, Screenshot

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('username', 'image',)

admin.site.register(Screenshot, ScreenshotAdmin)
