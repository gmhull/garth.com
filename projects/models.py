from django.db import models
from django.template.defaultfilters import slugify

class Project(models.Model):
    PROJECT_TOPICS = [
        ('ME', 'Engineering'),
        ('CS', 'Programming'),
        ('PE', 'Personal'),
        ('OT', 'Other')
    ]

    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True, null=False)
    type = models.CharField(max_length=15, choices=PROJECT_TOPICS, default='PE')
    date = models.DateTimeField()
    body = models.TextField()
    cover_image = models.ImageField()
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    body5 = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    img4 = models.ImageField(blank=True, null=True)
    img5 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
