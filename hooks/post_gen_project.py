#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess
import pathlib

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
project_dir = pathlib.Path(PROJECT_DIRECTORY)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.use_django }}' != 'y':
        configdir = project_dir / 'config/'
        import shutil
        shutil.rmtree(
            str(configdir
                ))  # must be converted to string for compat whith  python3.5

    print("Creating git repository (needed for PBR to fully work)")
    subprocess.check_call(["git", "init", "."])

    # Add a dir for sphinx
    staticdir = project_dir / 'docs/_static/'
    staticdir.mkdir(exist_ok=True)

    if '{{ cookiecutter.create_developer_env_after_scapfolding }}' == 'y':
        print("Setting up a virtual environment")
        subprocess.check_call(
            ["pipenv", "--python",
             str({{cookiecutter.python_version}})])
        subprocess.check_call(["pipenv", "install", "--dev"])

        print("Initial build...")
        venv = subprocess.check_output(["pipenv",
                                        "--venv"]).strip().decode('utf8')
        # Cannot use directly `pipenv run`, it requires a TTY, and the
        # --no-interactive options is not available on every version
        subprocess.check_call(
            [os.path.join(venv, "bin", "python"), "setup.py", "sdist"])

        print("Developer environment created. Activate with:")
        print("  pipenv shell")
        print(PROJECT_DIRECTORY)