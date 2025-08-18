from os import system
from api_config.settings.apps import PROJECT_APPS

if __name__ == "__main__":
    for app in PROJECT_APPS:
        system(f'python manage.py test {app}')