import abc
import pathlib

from .mixins import WithChildrenMixin, WithParentMixin


class BaseBlock(abc.ABC):
    """
    Abstract block class. Declares basic logic for all other block classes.

    This class defines the base functionality for all blocks, and is intended to be subclassed.
    """

    @abc.abstractmethod
    def to_str(self) -> str:
        """
        Convert block to string
        """

    def to_file(self, file: str | pathlib.Path, encoding: str = "utf-8") -> None:
        """
        Convert block to string and save it to file

        :param file: Target file, provided as Path object or string.
        :param encoding: Expected encoding of the target file, utf-8 by default.
        """
        block_str = self.to_str()
        with open(file, "w", encoding=encoding) as file_obj:
            file_obj.write(block_str)


class BaseParentBlock(BaseBlock, WithChildrenMixin, abc.ABC):
    """
    Abstract parent block class. Inherits from BaseBlock and WithChildrenMixin.

    This class extends the BaseBlock class to include functionality for managing children blocks.
    The WithChildrenMixin provides the ability to add, remove, and iterate over child blocks.
    """


class BaseChildBlock(BaseBlock, WithParentMixin, abc.ABC):
    """
    Abstract child block class. Inherits from BaseBlock and WithParentMixin.

    This class extends the BaseBlock class to include functionality for managing parent blocks.
    The WithParentMixin provides the ability to set and access the parent block.
    """


class BaseParentAndChildBlock(BaseBlock, WithParentMixin, WithChildrenMixin, abc.ABC):
    """
    Abstract block class that provides both parent and child functionality. Inherits from BaseBlock,
    WithParentMixin, and WithChildrenMixin.

    This class extends the BaseBlock class to include both parent and child functionality.
    The WithParentMixin provides the ability to set and access the parent block, while the
    WithChildrenMixin provides the ability to add, remove, and iterate over child blocks.
    """
