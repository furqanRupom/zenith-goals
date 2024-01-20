# Django Project startup

- set env for project

  ```bash
  py -m venv .venv

  ```

- Than Activate the env

  ```bash

  .venv/Scripts/activate

  ```

- you can deactivate it as well

```bash
       deactivate

```

## Install Django

- with this command

```bash
 py -m pip install Django

```

- update your pip package manager

```bash
 py -m pip install -U pip
```

<br>
<br>

## start project

- create django project

```bash
 django-admin startproject myproject
```

- move to project directory

```bash
 cd myproject
```

- run the server

```bash
 py manage.py runserver 8080
```

# Add static templates

## For this you have to do two things

### add this templates location -

```python

'DIRS': ['templates'],

```

```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]
```

### add static variables like that -

```python

# we include this static variable

STATIC_URL = 'static/'

# we also add this one as well

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

```

# Create new app

```bash
 py manage.py startapp
```

## Define app name in top level folder > settings.py

```py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts'
]

```

# you can add layout like that

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %} zenithGoals {% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
    <script src="{% static 'js/main.js' %}" defer></script>
  </head>
  <body>
    <nav>
      <a href="/">Home</a>
      <a href="/about">about</a>
      <a href="/posts">posts</a>
    </nav>

    <main>{% block content%} {% endblock %}</main>
  </body>
</html>
```

- then you can use it with extends property

```html
{% extends "layout.html" %} {% block title %} posts {% endblock %} {% comment %}
content here {% endcomment %} {% block content %}
<h1>Posts</h1>

{% endblock %}
```

# Define a database models in django

- First go to the inside of models file

- then write your necessary model like that

```py

from django.db import models

# Create your models here.

class Post(models.Model) :
  title = models.CharField(min_length = 5, max_length=255)
  description = models.TextField()
  slug = models.SlugField()
  date = models.DateField(auto_now=True)

```

# for migrations you can use this command -

```bash
py mange.py migrate

```

### for new models you have to make migrations first then you can apply any migration

```bash
py manage.py makemigrations

```

- response

```bash
  posts\migrations\0001_initial.py
    - Create model Post
```
