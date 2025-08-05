from django.db import models
from taggit.managers import TaggableManager

def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<slug>
    return 'recipes/%s/%s' % (instance.slug, filename)

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True, null=False)
    date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    cover_image = models.ImageField(upload_to=image_path)

    ingredients = models.TextField()
    description = models.TextField()
    instructions = models.TextField()
    servings = models.PositiveSmallIntegerField()
    time_to_make = models.PositiveSmallIntegerField()

    MEAL_TYPES = [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('Di', 'Dinner'),
        ('S', 'Snack'),
        ('De', 'Dessert')
    ]
    type = models.CharField(max_length=15, choices=MEAL_TYPES, default='D')

    tags = TaggableManager()

    def __str__(self):
        return self.title