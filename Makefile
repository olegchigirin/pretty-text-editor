verify-prerequisites:
	python ./development/ensure_dependencies.py

setup: verify-prerequisites
	poetry install --with dev

black:
	echo "Running black..."
	poetry run black ./src ./tests

isort:
	echo "Running isort..."
	poetry run isort ./src ./tests

isort-lint:
	echo "Running isort-lint..."
	poetry run isort --check-only ./src ./tests

mypy:
	echo "Running mypy..."
	poetry run mypy --python-version 3.10 --python-version 3.11 ./src ./tests

flake8:
	echo "Running flake8..."
	poetry run flake8 ./src ./tests

pylint:
	echo "Running pylint..."
	poetry run pylint ./src ./tests

format: black isort

lint: black isort-lint mypy flake8 pylint

test:
	echo "Running tests..."
	poetry run pytest

test-coverage:
	echo "Running tests with coverage..."
	poetry run pytest --cov