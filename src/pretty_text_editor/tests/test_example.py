"""
Example testing module.

The goal of this module is to check if pytest is working.
After the first real test is added, this module should be removed.
"""
from typing import NoReturn


def test_dummy() -> None | NoReturn:
    """
    Placeholder test to make sure pytest is working. Remove this test whenever you add your own real tests.
    """
    value: bool = True
    assert value, "Dummy test"
    return None
