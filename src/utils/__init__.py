from typing import NoReturn


def not_implemented(message: str = "Not implemented") -> NoReturn:
    """Placeholder for not implemented class fields."""
    raise NotImplementedError(message)
