from cookiecutter.main import cookiecutter
import sys

cookiecutter(
    'https://github.com/jgirardet/python-library-cookiecutter',
    no_input=True,
    extra_context={
        "python_version": sys.version[:3]
    })