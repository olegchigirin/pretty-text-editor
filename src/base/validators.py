"""
Module that contains all validators for the text block parameters.

All validators must be inherited from the AbstractParamValidator class.

All validators must be callable. They must accept a single argument - the value to validate.

They should be atomic and validated only one aspect of the parameter.
For example, the IsInteger validator should only check if the provided value is an integer.
It should not check if the value is not None. This should be done by the Required validator.
"""

__all__ = [
    "ParamValidator",
    "IsInteger",
    "Required",
]

import abc
from typing import Any, NoReturn

from .exceptions import IntegerParamRequired, ParamRequired


class ParamValidator(abc.ABC):
    """
    Abstract class for all validators.
    """

    def __call__(self, value) -> NoReturn | None:
        """
        Wrapper of the `_validation` method. Should be called to validate the provided value.
        Add some additional logic to the validation process.

        :param value: Value to validate.
        :raise ParamValidationError: If the value is not valid.
        """
        if value is None:
            return None
        return self._validate(value)

    @abc.abstractmethod
    def _validate(self, value) -> NoReturn | None:
        """
        Validation method.

        Should validate the provided value by validator rule

        :param value: value to validate
        :raise ParamValidationError: if the value is not valid
        """


class Required(ParamValidator):
    """
    Validate that the provided value is not None.
    """

    def __call__(self, *args, **kwargs) -> None | NoReturn:
        return self._validate(*args, **kwargs)

    def _validate(self, value: Any) -> None | NoReturn:
        if value is not None:
            return None
        raise ParamRequired()


class IsInteger(ParamValidator):
    """
    Validate the provided value for the provided parameter.
    """

    def _validate(self, value: str | None) -> None | NoReturn:
        if isinstance(value, int):
            return None
        raise IntegerParamRequired(f"Expected integer, gor {value} of type {type(value)}")
