.PHONY: build

MODULE:={{ cookiecutter.project_slug }}

all: dev style checks requirements build dists doc test-unit test-coverage

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

checks: sdist flake8 

flake8:
	pipenv run python setup.py flake8

build: dists

shell:
	pipenv shell

test-unit:
	pipenv run pytest 

test-coverage:
	pipenv run py.test  --cov $(MODULE) --cov-report term-missing --cov-report html

requirements:
	# needed until PBR supports `Pipfile`
	pipenv run pipenv_to_requirements

dists: requirements sdist wheels

sdist:
	pipenv run python setup.py sdist

wheels:
	pipenv run python setup.py bdist_wheel

pypi-publish: build
	pipenv run python setup.py upload -r pypi

update:
	pipenv update

githook: style requirements

push: githook
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
