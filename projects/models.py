from django.db import models
from django.template.defaultfilters import slugify

class Project(models.Model):
    PROJECT_TOPICS = [
        ('Engineering', 'Engineering'),
        ('Programming', 'Programming'),
        ('Personal', 'Personal'),
        ('Other', 'Other')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True, null=False)
    type = models.CharField(max_length=15, choices=PROJECT_TOPICS, default='PE')
    date = models.DateTimeField()
    # Make this a date field only
    body = models.TextField()
    cover_image = models.ImageField()
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    body5 = models.TextField(blank=True, null=True)
    img = models.ImageField(default="Default.png")
    img2 = models.ImageField(default="Default.png")
    img3 = models.ImageField(default="Default.png")
    img4 = models.ImageField(default="Default.png")
    img5 = models.ImageField(default="Default.png")

    def __str__(self):
        return self.title
