from django.db import models
from django.template.defaultfilters import slugify

def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<slug>
    return '%s/%s' % (instance.slug, filename)

class Project(models.Model):
    PROJECT_TOPICS = [
        ('Engineering', 'Engineering'),
        ('Programming', 'Programming'),
        ('Other', 'Other')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True, null=False)
    type = models.CharField(max_length=15, choices=PROJECT_TOPICS, default='PE')
    date = models.DateField()
    body = models.TextField()
    cover_image = models.ImageField(upload_to=image_path)
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    body5 = models.TextField(blank=True, null=True)
    img = models.ImageField(default="Default.png", upload_to=image_path)
    img2 = models.ImageField(default="Default.png", upload_to=image_path)
    img3 = models.ImageField(default="Default.png", upload_to=image_path)
    img4 = models.ImageField(default="Default.png", upload_to=image_path)
    img5 = models.ImageField(default="Default.png", upload_to=image_path)

    def __str__(self):
        return self.title
