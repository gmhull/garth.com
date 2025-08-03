from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager

def image_path_cover(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<slug>
    return '%s/%s' % (instance.slug, filename)

def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<slug>
    return '%s/%s' % (instance.project.slug, filename)

class Project(models.Model):
    PROJECT_TOPICS = [
        ('Art', 'Art'),
        ('Engineering', 'Engineering'),
        ('Programming', 'Programming'),
        ('Woodworking', 'Woodworking'),
        ('Other', 'Other')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True, null=False)
    type = models.CharField(max_length=15, choices=PROJECT_TOPICS, default='PE')
    date = models.DateField()
    cover_image = models.ImageField(upload_to=image_path_cover)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class ProjectPage(models.Model):
    project = models.ForeignKey(Project, related_name="pages", on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to=image_path, blank=True, null=True)


class Skills(models.Model):
    name = models.CharField(max_length=30)
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    icon_name = models.CharField(max_length=30)
    rating = models.PositiveSmallIntegerField(default=7, validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"