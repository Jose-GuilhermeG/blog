# Application definition

PROJECT_APPS = [
    'account',
    'core',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_INSTALLED_APPS = [
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    
]

INSTALLED_APPS = PROJECT_APPS + DJANGO_APPS + THIRD_INSTALLED_APPS