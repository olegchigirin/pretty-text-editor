"""
Base class describing any block of text used by the PrettyTextEditor package.

Block is an abstract idea that describes any text structure can be used for a creation of a document or a message.

For example, it could be a container containing other blocks, a text block, a table, a list, etc.
"""
import abc
from typing import NoReturn

from pretty_text_editor.base.exceptions import (
    ConflictDefinitionConflict,
    InvalidParam,
    RequiredParam,
)
from pretty_text_editor.utils import not_implemented

from .config_param import ConfigParam


class AbstractBlock(abc.ABC):
    """Default class that describes any block of text in a document or a message."""

    CONFIG: tuple[ConfigParam] = not_implemented("`CONFIG` property must be implemented in a subclass")
    __CONFIG_MAP: dict[str, ConfigParam] | None = None

    def __init__(self, **kwargs):
        self._validate_configuration()
        self._process_kwargs(**kwargs)
        for param, config in filter(lambda x: x[1] not in kwargs, self.map_config().items()):
            if config.default is not None and config.required:
                setattr(self, param, config.default)

    @classmethod
    def list_config(cls) -> tuple[ConfigParam]:
        """
        List of block configuration parameters that validates provided arguments.
        """
        return cls.CONFIG

    @classmethod
    def map_config(cls) -> dict[str, ConfigParam]:
        """
        Dictionary of block configuration parameters.
        """
        if not cls.__CONFIG_MAP:
            cls.__CONFIG_MAP = {param.name: param for param in cls.list_config()}
        return cls.__CONFIG_MAP

    def _validate_configuration(self) -> NoReturn | None:
        """
        Validate the configuration of the block.

        :raises ConflictDefinitionConflict: If the configuration has conflicts.
        """
        for param, config in self.map_config().items():
            if config.required and config.default is not None:
                raise ConflictDefinitionConflict(
                    f"Parameter {param} is required and has a default value. Please, remove one of them."
                )
        return None

    def _process_kwargs(self, **kwargs) -> NoReturn | None:
        """
        Process provided parameters.

        :param kwargs: Provided configuration parameters.

        :raises InvalidParam: If the provided parameter is not expected.
        :raises ParamValidationError if the provided parameter is not valid.
        """
        for param, value in kwargs.items():
            try:
                param_config = self.map_config()[param]
                for validator in param_config.validators:
                    validator(value)
                setattr(self, param, value)
                return None
            except KeyError as exc:
                raise InvalidParam(
                    f"Unexpected {param=} ({value=}). Expected parameters: {', '.join(self.map_config())}"
                ) from exc

    def _process_required_and_default(self, **kwargs) -> NoReturn | None:
        for param, config in filter(lambda x: x[1] not in kwargs, self.map_config().items()):
            if config.required:
                raise RequiredParam(f"Required parameter {param} is not provided.")
            if config.default is not None:
                setattr(self, param, config.default)
        return None
