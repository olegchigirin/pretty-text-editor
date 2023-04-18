import abc
from typing import Any, NoReturn


class ParamValidator(abc.ABC):
    """
    Abstract class for all validators.
    """

    def __call__(self, value: Any) -> NoReturn | None:
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
    def _validate(self, value: Any) -> NoReturn | None:
        """
        Validation method.

        Should validate the provided value by validator rule

        :param value: value to validate
        :raise ParamValidationError: if the value is not valid
        """
