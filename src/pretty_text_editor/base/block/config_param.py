"""
Module containing the specification class of the block configuration parameter.
"""

__all__ = [
    "ConfigParam",
]

from typing import Any, NamedTuple

from ..validators import ParamValidator


class ConfigParam(NamedTuple):
    """
    Specification of the block configuration parameter.

    :param name: Name of the parameter.
    :param validators: List of validators that should be applied to the parameter.
    :param default: Default value of the parameter.
    :param required: Whether the parameter is required or not.
    """

    name: str
    """Name of the parameter."""
    required: bool = False
    """Whether the parameter is required or not."""
    validators: list[ParamValidator] = []
    """List of validators that should be applied to the parameter."""
    default: Any | None = None
    """Default value of the parameter. Conflicts with `required` parameter."""
