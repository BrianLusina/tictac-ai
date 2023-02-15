setup:
	python3 -m venv .venv
	source .venv/bin/activate

install:
	pip install --upgrade pip
	pip install poetry
	cd tictacai && poetry install

test:
	pytest

test-cover:
	pytest --cov=tictacai tictacai/tests/

precommit:
	pre-commit run --verbose --all-files --show-diff-on-failure

lint:
	black tictacai
	black clients

# Build application
build:
	cd tictacai && python setup.py sdist bdist_wheel && poetry build

all: setup install lint test build