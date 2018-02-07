from .base import *

#Use this with for sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

#If postgree is configured in .env, you only need it to use pg.
# DATABASES['default']['NAME'] = 'test'
