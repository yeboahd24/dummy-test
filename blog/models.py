from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=300)
    slug = models.SlugField(max_length=30, unique=True)


    def __str__(self):
        return self.title