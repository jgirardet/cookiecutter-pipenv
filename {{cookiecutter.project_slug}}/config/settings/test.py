from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
#to use  if postregsql is  via a .env file.
#DATABASES['default']['NAME'] = 'test'
