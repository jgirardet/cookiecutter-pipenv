import sys

from cookiecutter.main import cookiecutter
import pathlib
import os
"""
just launch a cookie cookiecutter
dont-t change my_project_name
"""
if __name__ == '__main__':
    try:
        os.environ['CI']  #is continus integration ?
    except KeyError:
        cookie_path = sys.argv[
            1]  #if yes give the path to the build downloaded from git
    else:
        cookie_path = os.environ['TRAVIS_BUILD_DIR']
    print(cookie_path)
    extra_context = {
        "python_version": sys.version[:3],  # install with travis python V
        "create_developer_env_after_scapfolding": "n",
    }
    if float(sys.version[:3]) < 3.6:
        extra_context[
            'use_apistar'] = "n"  #do not test apistar under python3.6

    cookiecutter(
        cookie_path,
        no_input=True,
        # install specifique version en travis and pipenv bug under travis, make all does the job next
        extra_context=extra_context)
