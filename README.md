# pretty-text-editor

Useful tools to simplify formatting on txt files and messages

# Requirements

* Python 3.10 or higher
* Python pip
* Poetry

## Useful tools

* [PyEnv](https://github.com/pyenv/pyenv) - Python version manager
* [PyEnv for Windows](https://github.com/pyenv-win/pyenv-win) - Python version manager for Windows

# Installation

## Local development

### Windows

1. Install Python 3.10 or higher
2. Install Python pip
3. Clone the repository
4. Open a terminal in the repository folder
5. Create a virtual environment with `python -m venv venv`
6. Activate the virtual environment with `venv\Scripts\activate.bat`
7. Create virtual environment and install dependencies with `poetry install`

### Linux

#### Console flow

1. Install Python 3.10 or higher
2. Install Python pip
3. Clone the repository
4. Open a terminal in the repository folder
5. Create a virtual environment with `python -m venv venv`
6. Activate the virtual environment with `source venv/bin/activate`
7. Create virtual environment and install dependencies with `poetry install`

#### Using Makefile

1. Install Python 3.10 or higher
2. Install Python pip
3. Clone the repository
4. Open a terminal in the repository folder
5. Run `make setup`

## Dependencies management

As a dependency manager, Poetry is used.
* To install a new dependency, run `poetry add <dependency>`.
* To remove a dependency, run `poetry remove <dependency>`.
* To update a dependency, run `poetry update <dependency>`.

See [Poetry documentation](https://python-poetry.org/docs/managing-dependencies/) for more information.
