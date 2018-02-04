import sys

from cookiecutter.main import cookiecutter
import pathlib
import os
"""
just launch a cookie cookiecutter
dont-t change my_project_name
"""
if __name__ == '__main__':
    ci = os.environ['CI']
    print(ci)
    if ci:
        cookie_path = os.environ['TRAVIS_BUILD_DIR']
    else:
        cookie_path = sys.argv[1]

    cookiecutter(
        cookie_path,
        no_input=True,
        # install specifique version en travis and pipenv bug under travis, make all does the job next
        extra_context={
            "python_version": sys.version[:3],
            "create_developer_env_after_scapfolding": "n",
        })
    """
    .env has to be created at start of project

    """
    chemin = pathlib.Path("my_project_name/.env")
    chemin.touch()
    chemin.write_text(
        "DB_ENGINE=django.db.backends.sqlite3\nDB_NAME=db.local\nSECRET_KEY=mokmokmok"
    )