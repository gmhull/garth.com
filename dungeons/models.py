from django.db import models

# Create your models here.
class Level(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    floor_number = models.CharField(max_length=2)
    slug = models.SlugField(max_length=10, null=False, unique=True)
    map = models.ImageField(upload_to='dnd')
    color = models.CharField(max_length=10, default="black")
    answer = models.CharField(max_length=50)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'Level: {self.id}'

    def password_check(self, answer):
        if self.answer.lower() == answer.lower():
            return True
        return False
