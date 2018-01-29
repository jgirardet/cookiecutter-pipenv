Stibons 2017 OpenSource Python Library Cookiecutter
===================================================

.. image:: https://travis-ci.org/Stibbons/python-library-cookiecutter.svg?branch=master
    :target: https://travis-ci.org/Stibbons/python-library-cookiecutter

Cookie cutter recipe for bootstrapping an OpenSource Python **library** using state of the art,
free services and the best "opensource" mindset.

Library vs Application
----------------------

It is important to differentiate a Python "Library" and a Python "Application". Each form have its
own life and should handle dependencies differently:

- To ensure stability and reproductibility of the deployment of an **application**, a good practice
  is to **freeze the versions of all its dependencies**, so, no matter what happens for example on
  https://pypi.python.org for example a new, buggy version of a package your application relies on
  actually break your application. Without proper "frozen" dependencies management, you might get
  this dependency library deployed on production without any validation.

- for a **library**, dependencies versions should not be frozen and should be defined using version
  ranges.
  For example, let's imagine your library depends on a module A in version 1.0. Your library is
  then used in an application that also depends on the same module A, but in version 1.2. The best
  way to handle this is to let libraries describe the range of supported versions, and let the
  package manager (Pip) find the best candidates.


Python Library Receipe Features
------------------------------

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.

Feature of the "Python Library" Cookiecutter recipe:

- Use **Pipenv** to manage ``Pipfile``.
- Dependencies are defined by range and ``Pipfile.lock`` is **not** tracked
- ``requirements.txt`` and ``requirements-dev.txt`` are AUTOMATICALLY generated for services
  such as ReadTheDocs that does not support ``Pipfile`` yet.
- Source code is horst on **Github**
- Free software: **MIT license**
- **Badges** for Travis, Coverage, Pypi, ReadTheDoc
- Python 2, 3 and Pypy, with default set to Python 3
- **PBR**: handle automatic versioning based on Git Tag, automatic creation of `ChangeLog` and
  `AUTHORS` files
- **Pypi**: automatic deployment of distribution package or wheels on successful Travis Tag build
- **Makefile** to ease daily-life of developers and maintainers
- **Travis-CI**: build, unit test
- **Automatically deploy successful tagged version** to Pypi
- **Automatically set Travis CI deployment token** with `travis_pypi_setup.py` script
- **isort, Yapf, AutoPep8**: code formatting
- **Pylint, Flake8**: code style
- **Editorconfig**: autoconfiguration of almost any editor
- **Coverage**: unit test report
- Use **Pytest** and **Tox** for Unit testing
- **Sphinx docs**: Documentation ready for generation and publication to **ReadTheDoc**

Usage
-----

Do not create a folder for your project, it will be automatically created.

Boostrap your Python library:

    .. code-block:: bash

        $ pip3 install --user --upgrade pip cookiecutter

        $ cookiecutter https://github.com/Stibbons/python-library-cookiecutter

        # or

        $ cookiecutter gh:Stibbons/python-library-cookiecutter

Setup for development:

    .. code-block:: bash

        $ make dev

Note

    Deploying a "library" in production has little to no meaning. If it is intended to be deployed
    directly on the system, use your distribution package manager (`apt`, 'brew', 'yum', ...)

    If it is meant to be deployed alongside with an application, it should be installed from the
    Pypi repository (or a cache) and installed into the Virtualenv this application will use.

Execute unit tests:

    .. code-block:: bash

        $ make test

Build package (source, binary and wheels):

    Use it for most package without low level system dependencies.

    .. code-block:: bash

        make dists

To register Pipy deployment:

- commit your work!
- enable your project on Travis
- execute ``pipenv run python travis_pypi_setup.py``

Create a release:

    .. code-block:: bash

        make release
        git tag 1.2.3
        make push

On successful travis build on the Tag branch, your Pypi package will be updated automatically.

Configuration
-------------

You will need to configure `.travis.yml` to enable automatic PyPi deployment, or use the provided
`travis_pypi_setup.py` script.

ChangeLog after Fork
----------------------
- tests out of package directory
- config folder for django only
- REMOVED .env from .gitignore
- added package path to python path in .env (for tests, doc and package)
- travis start at python 3.5
- subversion of python at install (3.5, 3.6 etc)
- Sphinx
- Makefile added docs command
- Pipfile : django conditionnal 
- setup.cfg : doc directory
- remove pylint