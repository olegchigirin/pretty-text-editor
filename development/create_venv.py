def create_venv() -> None:
    """
    Create a virtual environment.

    If a path is not specified, the default `venv` location is used.
    If a relative path is specified, it is relative to the current directory.
    If an absolute path is specified, it can be outside the current directory.

    :raises RuntimeError: If the virtual environment cannot be created.
    """
    from venv import create
    import pathlib
    import sys

    path_from_cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if not path_from_cmd:
        venv_path = pathlib.Path('venv')
    else:
        venv_path = pathlib.Path(path_from_cmd)
    if not venv_path.is_absolute():
        venv_path = pathlib.Path(__file__).parent.parent / venv_path
    create(venv_path, with_pip=True)
    print(f"Virtual environment created at {venv_path}.")


if __name__ == "__main__":
    create_venv()
