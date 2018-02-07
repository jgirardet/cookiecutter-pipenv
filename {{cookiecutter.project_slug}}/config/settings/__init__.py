# -*- coding: utf-8 -*-
import os
from .get_env import env
import django
from django.apps import apps

# define this is needed by django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
"""
We check environment.
If pytest then test environment.
else local or prod denpending DEBUG
"""

try:
    os.environ['PYTEST_VER']  #given by pytest-env-info
except KeyError:
    if env['DEBUG'] == True:
        print('local config loaded')
        from .local import *
    else:
        print('prod config loaded')
        from .prod import *
else:
    print('test config loaded')
    from .test import *

if SECRET_KEY == "please_change_it":
    print("""
##################################
# YOU MUST CHANGE YOU SECRET KEY #
##################################
#Add  SECRET_KEY to local or prod#
#      or set it in .env         #
##################################
""")

if DEBUG:
    print("""
##################################
#     DEBUG MODE IS ACTIVE       #
##################################
""")

# needed
if not apps.ready:
    django.setup()