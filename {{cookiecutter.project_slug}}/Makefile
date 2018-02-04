.PHONY: build

MODULE:={{ cookiecutter.project_slug }}

all: dev style checks requirements.txt {% if cookiecutter.use_apistar == 'y' %}migrate{% endif %} build dists doc test-unit test-coverage

dev:
	pipenv install --dev --python {{cookiecutter.python_version}}

install-local:
	pipenv install --python {{cookiecutter.python_version}}

install-system:
	pipenv install --system

style: isort autopep8 yapf

isort:
	pipenv run isort -y

autopep8:
	pipenv run autopep8 --in-place --recursive setup.py $(MODULE)

yapf:
	pipenv run yapf --style .yapf --recursive -i $(MODULE)

checks:
	pipenv check

flake8:
	pipenv run python setup.py flake8

build: dists

shell:
	pipenv shell

test-unit:
	pipenv run pytest 

test-coverage:
	pipenv run py.test  --cov $(MODULE) --cov-report term-missing --cov-report html

requirements.txt:
	{% if cookiecutter.library_or_app == 'libray' %}
	# generate requirements.txt from Pipfile
	# needed until PBR supports `Pipfile`
	pipenv run pipenv_to_requirements
	{% endif %}
	{% if cookiecutter.library_or_app == 'app' %}
	# generate requirements.txt frm Pipfile.lock
	# needed until PBR supports `Pipfile`
	pipenv run pipenv_to_requirements -f
	{% endif %}

Pipfile.lock:	Pipfile
	pipenv lock

dists: requirements.txt sdist wheels

sdist:
	pipenv run python setup.py sdist

wheels:
	pipenv run python setup.py bdist_wheel

pypi-publish: build
	pipenv run python setup.py upload -r pypi

update:
	pipenv update

githook: checks style requirements.txt
	
push: githook
	git status
	git push origin --all
	git push origin --tags

doc:
	pipenv run python setup.py build_sphinx

doc-auto:
	pipenv run sphinx-autobuild docs docs/_build
	
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

{% if cookiecutter.use_apistar == 'y' %}
migrate: migrations
	pipenv run python manage.py migrate

migrations:
	pipienv run python manage.py makemigrations
{% endif %}

# aliases to gracefully handle typos on poor dev's terminal
check: checks
devel: dev
develop: dev
dist: dists
install: install-system
pypi: pypi-publish
styles: style
test: test-unit
unittest: test-unit
wheel: wheels
