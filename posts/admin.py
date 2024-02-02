from django.contrib import admin
from .models import Post

# Register your models here.

# we have to add all the necessary models in this file

admin.site.register(Post)
