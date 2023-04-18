from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pretty_text_editor.block import AbstractBlock


class WithChildrenMixin(abc.ABC):
    """
    Mixin class that provides the ability to have children blocks for the class.
    """

    _children: list[AbstractBlock]

    @property
    def children(self) -> list[AbstractBlock]:
        """
        List of children blocks.
        """
        return self._children

    @children.setter
    def children(self, value: list[AbstractBlock]) -> None:
        """
        Set the list of children blocks.

        :param value: List of children blocks.
        """
        self._children = value
