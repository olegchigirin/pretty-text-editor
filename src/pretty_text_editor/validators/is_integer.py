from typing import NoReturn

from pretty_text_editor.exceptions import IntegerParamRequired

from .param_validator import ParamValidator


class IsInteger(ParamValidator):
    """
    Validate the provided value for the provided parameter.
    """

    def _validate(self, value: str | None) -> None | NoReturn:
        if isinstance(value, int):
            return None
        raise IntegerParamRequired(f"Expected integer, gor {value} of type {type(value)}")
