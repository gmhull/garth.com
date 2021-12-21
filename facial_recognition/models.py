from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    """Adding to the default user class."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dungeon_depth = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    MAX_LEVEL = 10

    def __str__(self):
        return f'{self.user.username} is on level {self.dungeon_depth}'

    def delve_down(self):
        if self.dungeon_depth < self.MAX_LEVEL:
            self.dungeon_depth += 1
            self.save(update_fields=['dungeon_depth'])
        elif self.dungeon_depth == self.MAX_LEVEL:
            self.completed = True
            self.save(update_fields=['completed'])
            return True
        return False

class Screenshot(models.Model):
    """Image class is used to get image from html to django backend."""
    username = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
