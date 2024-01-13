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



###  add this templates location -

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



## Define app name in top level folder >  settings.py

```python

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