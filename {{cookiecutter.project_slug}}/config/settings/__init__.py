# -*- coding: utf-8 -*-
from config.get_env import env

if not env['TEST_RUNNING']:
    if env['DEBUG']:
        print("\n ### Apistar'' LOCAL config loaded ###  \n")
        from .local import *
    else:
        print("\n ### Apistar PRODUCTION config loaded ###  \n")
    from .prod import *
else:
    print("\n ### Apistar TESTING config loaded ###  \n")
    from .testing import *

if env['DEBUG']:
    print("""
##################################
#     DEBUG MODE IS ACTIVE       #
##################################
""")
