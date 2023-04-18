"""
Module that contains all validators for the text block parameters.

All validators must be inherited from the AbstractParamValidator class.

All validators must be callable. They must accept a single argument - the value to validate.

They should be atomic and validated only one aspect of the parameter.
For example, the IsInteger validator should only check if the provided value is an integer.
It should not check if the value is not None. This should be done by the Required validator.
"""

from .is_integer import IsInteger
from .param_validator import ParamValidator
