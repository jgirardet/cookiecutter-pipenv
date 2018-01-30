from cookiecutter.main import cookiecutter
import sys
"""
just launch a cookie cookiecutter
"""

cookiecutter(
    'https://github.com/jgirardet/python-library-cookiecutter',
    no_input=True,
    extra_context={
        "python_version": sys.version[:3],
        "create_developer_env_after_scapfolding": "n",
    })