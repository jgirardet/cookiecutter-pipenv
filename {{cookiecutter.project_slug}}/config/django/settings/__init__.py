from config.get_env import env

if not env['TEST_RUNNING']:
    if env['DEBUG']:
        print("\n ## Django LOCAL config loaded ###  \n")
        from .local import *
    else:
        print("\n ## Django PRODUCTION config loaded ###  \n")
    from .prod import *
else:
    print("\n ## Django TESTING config loaded ###  \n")
    from .testing import *

if SECRET_KEY == "youshouldchangeit":
    print("""
##################################
# YOU MUST CHANGE YOU SECRET KEY #
##################################
#Add  SECRET_KEY to local or prod#
#      or set it in .env         #
##################################
""")