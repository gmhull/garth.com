from django.db import models

# Create your models here.
class Level(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    floor_number = models.CharField(max_length=2)
    slug = models.SlugField(max_length=10, null=False, unique=True)
    map = models.ImageField(upload_to='dnd')
    color = models.CharField(max_length=10, default="black")

    def __str__(self):
        return self.title
