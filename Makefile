setup:
	python3 -m venv .venv
	source .venv/bin/activate

install-poetry:
	pip install --upgrade pip
	pip install poetry
	poetry install

test:
	pytest

test-cover:
	pytest --cov=tictacai tests/

precommit:
	pre-commit run --verbose --all-files --show-diff-on-failure

lint:
	black tictacai
	black clients

license-check:
    # Reference: https://pypi.org/project/pip-licenses/
	pip-licenses --fail-on="GPL License" --format=markdown --with-urls --with-description

# Build application
build:
	python setup.py sdist bdist_wheel
	poetry build

all: setup install-poetry lint test build