MINIMUM_PYTHON_VERSION = (3, 10)
TOOL_REQUIREMENTS = ['pip', 'make', 'poetry']


def validate_requirements() -> None:
    """Validate that the required dependencies are installed."""
    import sys
    import shutil

    if sys.version_info < MINIMUM_PYTHON_VERSION:
        raise RuntimeError(f'Unsupported Python version: {sys.version}')

    missing_tools = []
    for tool in TOOL_REQUIREMENTS:
        if shutil.which(tool) is None:
            missing_tools.append(tool)

    if missing_tools:
        raise RuntimeError("Several tools are not installed: " + ", ".join(missing_tools))

    tools_message = ";\n".join(f"{tool}: {shutil.which(tool)}" for tool in TOOL_REQUIREMENTS)
    message = f"""\
All requirements are satisfied.
Current setup:
Python: {sys.version}
Tools: 
{tools_message}
"""
    print(message)


if __name__ == "__main__":
    validate_requirements()
