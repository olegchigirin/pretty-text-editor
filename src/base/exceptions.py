"""
Exception classes used by the PrettyTextEditor package.

All of them are derived from the PTextEditorValidationError class, which is a subclass of the Exception class.
"""

__all__ = [
    "PrettyTextEditorException",
    "InvalidParam",
    "RequiredParam",
    "ConflictDefinitionConflict",
    "ParamValidationError",
    "IntegerParamRequired",
]

import abc


class PrettyTextEditorException(Exception, abc.ABC):
    """Default exception class for the PrettyTextEditor"""


class InvalidParam(PrettyTextEditorException):
    """Exception class for the case when an unexpected parameter is provided."""


class RequiredParam(PrettyTextEditorException):
    """Exception class for the case when a required parameter is not provided."""


class ConflictDefinitionConflict(PrettyTextEditorException):
    """Exception class for the case when a parameter configuration definition has conflicts."""


class ParamValidationError(PrettyTextEditorException, abc.ABC):
    """Exception class for the case when a parameter validation fails."""


class IntegerParamRequired(ParamValidationError):
    """
    Exception class for the case when a value is not an integer. Used in case parameters must be integers.
    """

    def __init__(self, message: str = "Integer value is required") -> None:
        super().__init__(message)
