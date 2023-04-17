SRC = $(shell pwd)

verify-prerequisites:
	python $(SRC)/development/ensure_dependencies.py

create_venv $(VENV_PATH):
	python $(SRC)/development/create_venv.py $(VENV_PATH)

setup $(VENV_PATH): verify-prerequisites create_venv