from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..base import BaseBlock


class WithParentMixin(abc.ABC):
    """
    Mixin that allows block to have a parent block.
    """

    _parent: BaseBlock | None = None

    @property
    def parent(self) -> BaseBlock | None:
        """
        Get the parent block of the current block.

        :return: The parent block of the current block, if it exists.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: BaseBlock | None) -> None:
        """
        Set the parent block of the current block.

        :param parent: The parent block of the current block.
        """
        self._parent = parent
