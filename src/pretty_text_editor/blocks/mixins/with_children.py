from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Iterable, TypeAlias

from typing_extensions import Self

if TYPE_CHECKING:
    from ..base import BaseBlock

_BlockName: TypeAlias = str


class WithChildrenMixin(abc.ABC):
    """
    Mixin for blocks that can have child blocks.
    """

    _children: dict[_BlockName, BaseBlock] | None = None

    @property
    def children(self) -> dict[_BlockName, BaseBlock]:
        """
        Returns a dictionary of child blocks for this block.
        """
        if self._children is None:
            self._children = {}
        return self._children

    def add_child(self, block: BaseBlock, name: _BlockName) -> Self:
        """
        Adds a child block to this block.

        :param block: The child block to add.
        :param name: The name of the child block.
        """
        if self._children is None:
            self._children = {}
        self._children[name] = block
        return self

    def remove_child(self, name: _BlockName) -> Self:
        """
        Removes a child block from this block.

        :param name: The name of the child block to remove.
        """
        if self._children is None:
            return self
        if name not in self._children:
            return self
        self._children.pop(name)
        return self

    def clear_children(self) -> Self:
        """
        Removes all child blocks from this block.
        """
        if self._children is not None:
            self._children.clear()
        return self

    def has_children(self) -> bool:
        """
        Returns True if this block has any child blocks.
        """
        return bool(self._children)

    def iter_children_names(self) -> Iterable[_BlockName]:
        """
        Returns an iterator over the names of this block child blocks.
        """
        for child_name in self.children:
            yield child_name

    def iter_children(self) -> Iterable[BaseBlock]:
        """
        Returns an iterator over this block child blocks.
        """
        for child in self.children.values():
            yield child
