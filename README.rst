.. image:: https://travis-ci.org/jgirardet/cookiecutter-pipenv.svg?branch=master
    :target: https://travis-ci.org/jgirardet/cookiecutter-pipenv
    

A pipenv friendly cookie-cutter template
===================================================

Pipenv should be the new standard but there isn't much template to deal with.

This Cookie Cutter template is very inspirated from https://github.com/gsemet/python-library-cookiecutter.
Thanks to gsemet for his work.

I created a new one because it was becoming to much different from the python-library-cookiecutter.

It's realy for python >3.5. I don't know if previous is ok.

What's included ?
------------------------------

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.


- Use **Pipenv** to manage ``Pipfile``.
- Dependencies are defined by range and ``Pipfile.lock`` is tracked
- ``requirements.txt`` and ``requirements-dev.txt`` are AUTOMATICALLY generated for services
  such as ReadTheDocs that does not support ``Pipfile`` yet.
- Source code is horst on **Github**
- Free software: **GPL, MIT, ...**
- **Badges** for Travis, Coverage, Pypi, ReadTheDoc
- You choose your vesion of python at install : **3.5, 3.6** 
- **PBR**: handle automatic versioning based on Git Tag, automatic creation of `ChangeLog` and
  `AUTHORS` files
- **Pypi**: automatic deployment of distribution package or wheels on successful Travis Tag build
- **Makefile** to ease daily-life of developers and maintainers
- **Travis-CI**: build, unit test
- **Automatically deploy successful tagged version** to Pypi
- **Automatically set Travis CI deployment token** with `travis_pypi_setup.py` script
- *eisort, Yapf, AutoPep8**: code formatting
- **flake8**: code style
- **Coverage**: unit test report
- Use **Pytest** for Unit testing
- **Sphinx docs**: Documentation ready for generation and publication to **ReadTheDoc**
- controle package security with **pyup**.
- 


Get Started:
--------------

Do not create a folder for your project, it will be automatically created.


    .. code-block:: bash

        $ pip3 install --user --upgrade pipenv cookiecutter

        $ cookiecutter https://github.com/jgirardet/cookiecutter-pipenv

At start it will ask you for libray or app.
This is important depending the way you want dependencies work.
Libray will use Pipfile as requirements.txt, so if put django="\*" the newest version wil be used.
App will use Pipfile.lock as requirements.txt, it will put the exact version you are running (ex : django(1.11.3).
This behaviour tries to do **soft** dependencies for libray but **strong** dependencies for applications.
This will work only if  you use ``make push`` instead of ``git push`` because ``make push`` generates the requirements.txt




Step 2:
---------


Setup for development:

Juste chose *create_developer_env_after_scapfolding*. You can Also type :
    .. code-block:: bash

        $ make dev

Step 3:
--------
- commit your work!
- create a github repo
- enable your project on Travis
- execute ``pipenv run python travis_pypi_setup.py`` if you want auto deployement of new version on Pypi
- enable on read the docs if needed
- enable your coverall account
- enable you pyup account
- push all with : ``make push``



Usage:
-------


Run tests
  .. code-block:: bash
  
      make test 
      make test-coverage

  depending what you want.


Build package (source, binary and wheels):
  Use it for most package without low level system dependencies.

    .. code-block:: bash

        make dists


Create a release:
    .. code-block:: bash

        # commit your work
        git tag 1.2.3
        make push

  If requirements.txt isn't up to date it will generate requirements.txt but not commit it. Git will tell you that. The thing to do is to commit the changes and execute ``make push`` again.
  On successful travis build on the Tag branch, your Pypi package and ReadTheDoc will be updated automatically.


Make the Doc:
  .. code-block:: bash

        make doc

  One time generation


  .. code-block:: bash

      make doc-auto

  This launch a mini server and doc is rebuild for each change.
  readTheDoc neads requirements files so you need to a ``make requirements`` or ``make all`` to make it work. 

Clean everything:
  .. code-block:: bash
  
      make clean

Django option:
  this add:
  
  - repo config for settings, urls...
  - adjust the doc. doc won't work if you say no to django  but then you install anyway
  - add package : 

    + pytest-django
    + pytest-pythonpath: django wants config in path
    + django-reset-migrations: allways usefull
    + django-extensions : for shell_plus  server_plus 
    + todo : manage.py, urls

Asyncio:
  Not tested, don't no if it's working

What does make push do ?
  - style with : Yapf, AutoPep8 and flake8
  - check pep 508
  - use safety from  https://github.com/pyupio/safety
  - autogenerate requirements.txt and requirements-dev.txt
  - git status : to show if some uncommited things
  - push commits and tags



Contributing
----------------
You're welcome



ChangeLog after Fork
----------------------
- tests out of package directory
- config folder for django only
- travis start at python 3.5
- subversion of python at install (3.5, 3.6 etc)
- Sphinx
- Makefile added docs command
- Pipfile : django conditionnal 
- setup.cfg : doc directory
- remove pylint
- pytest-pythonpath + pytest.ini
- make doc-auto : sphinx-autobuild
- Pipfile.lock is not ignored anymore  by default
- write oc : lounc pipi with pipenv 
- package is library or app
