verify-prerequisites:
	python ./development/ensure_dependencies.py

setup: verify-prerequisites
	poetry install --with dev