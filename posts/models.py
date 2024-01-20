from django.db import models

# Create your models here.

class Post(models.Model) :
  title = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField()
  date = models.DateField(auto_now=True)
