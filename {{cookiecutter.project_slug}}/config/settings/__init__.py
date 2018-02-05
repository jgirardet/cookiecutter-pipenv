# -*- coding: utf-8 -*-
import os
from .get_env import env
import django
from django.apps import apps

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

if env['DEBUG'] == True:
    from .local import *
else:
    from .prod import *

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

if not apps.ready:
    django.setup()