"""
Base class describing any block of text used by the PrettyTextEditor package.

Block is an abstract idea that describes any text structure can be used for a creation of a document or a message.

For example, it could be a container containing other blocks, a text block, a table, a list, etc.
"""
import abc
import dataclasses
from typing import Any

from .validators import ParamValidator


@dataclasses.dataclass
class _Param:
    """
    Specification of the block configuration parameter.

    :param name: Name of the parameter.
    :param validators: List of validators that should be applied to the parameter.
    :param default: Default value of the parameter.
    """

    name: str
    validators: list[ParamValidator] = dataclasses.field(default_factory=list)
    default: Any | None = None


class AbstractBlock(abc.ABC):
    """Default class that describes any block of text in a document or a message."""

    CONFIG: list[_Param]

    def __init__(self, **kwargs):
        for prop in self.CONFIG:
            value = kwargs.get(prop.name, prop.default)
            for validator in prop.validators:
                validator(value)
            setattr(self, prop.name, value)

    @classmethod
    def get_config(cls) -> list[_Param]:
        """List of block configuration parameters that validates provided arguments."""
        return cls.CONFIG
