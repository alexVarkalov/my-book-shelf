from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'django/common.py',
    'django/installed_apps.py',
    'django/middleware.py',
    'django/common.py',
    'django/database.py',
    'django/templates.py',
]

include(*base_settings)
