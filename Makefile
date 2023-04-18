verify-prerequisites:
	python ./development/ensure_dependencies.py

setup: verify-prerequisites
	poetry install --with dev

black:
	echo "Running black..."
	poetry run black ./src

isort:
	echo "Running isort..."
	poetry run isort ./src

isort-lint:
	echo "Running isort-lint..."
	poetry run isort --check-only ./src

mypy:
	echo "Running mypy..."
	echo "Python 3.10..."
	poetry run mypy --python-version 3.10 ./src
	echo "Python 3.11..."
	poetry run mypy --python-version 3.11 ./src

flake8:
	echo "Running flake8..."
	poetry run flake8 ./src

pylint:
	echo "Running pylint..."
	poetry run pylint ./src

format: black isort

lint: black isort-lint mypy flake8 pylint

test:
	echo "Running tests..."
	poetry run pytest

test-coverage:
	echo "Running tests with coverage..."
	poetry run pytest --cov