from django.db import models

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
    cover_image = models.ImageField(upload_to=image_path)

    def __str__(self):
        return self.title


class ProjectPage(models.Model):
    project = models.ForeignKey(Project, related_name="pages", on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to=image_path, blank=True, null=True)