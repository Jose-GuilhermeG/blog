from .basic_configs import env

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": "3306",
        "ATOMIC_REQUESTS" : True
    },
    'test' : {
        'NAME' : f'test_{env("DATABASE_NAME")}'
    }
}