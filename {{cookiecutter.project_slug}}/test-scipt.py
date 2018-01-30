from cookiecutter.main import cookiecutter
import sys

cookiecutter(
    'cookiecutter-django',
    no_input=True,
    extra_context={
        "python_version": sys.version[:3]
    })