from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pretty_text_editor.block import AbstractBlock


class WithParentMixin(abc.ABC):
    """
    Mixin class that provides the ability to have parent block for the class.
    """

    _parent: AbstractBlock | None = None

    @property
    def parent(self) -> AbstractBlock | None:
        """
        Parent block.
        """
        return self._parent

    @parent.setter
    def parent(self, value: AbstractBlock | None) -> None:
        """
        Set the parent to the block.

        :param value: Parent block.
        """
        self._parent = value
