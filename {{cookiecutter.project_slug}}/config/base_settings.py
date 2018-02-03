DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local_db',
    },
}

INSTALLED_APPS = [
    'pseudos',
]

SECRET_KEY = 'mzeokfmzoekfmozekf'
# added for manage.py only
DEBUG = True
