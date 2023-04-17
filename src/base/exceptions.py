"""
Exception classes used by the PrettyTextEditor package.

All of them are derived from the PTextEditorValidationError class, which is a subclass of the Exception class.
"""

__all__ = [
    "PrettyTextEditorException",
    "ParamValidationError",
    "ParamRequired",
    "IntegerParamRequired",
]

import abc


class PrettyTextEditorException(Exception, abc.ABC):
    """Default exception class for the PrettyTextEditor"""


class ParamValidationError(PrettyTextEditorException):
    """Exception class for the case when a parameter validation fails."""


class ParamRequired(ParamValidationError):
    """
    Exception class for the case when a value is not specified. Used in case parameters are required.
    """

    def __init__(self, message: str = "Value is not specified") -> None:
        super().__init__(message)


class IntegerParamRequired(ParamValidationError):
    """
    Exception class for the case when a value is not an integer. Used in case parameters must be integers.
    """

    def __init__(self, message: str = "Integer value is required") -> None:
        super().__init__(message)
