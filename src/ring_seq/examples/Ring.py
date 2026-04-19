"""Contains the example `Ring` class.

Usage example:

  >>> r = Ring([1, 2, 3])
  >>> r.rotate_l(1)
  >>> r.current()
  [2, 3, 1]
"""
from typing import Any

from ring_seq import IndexO, RingSeq


class Ring:
    """An example class wrapping a sequence and keeping mutable states of rotation and reflection.

    Attributes:
        underlying: The wrapped `RingSeq`.
        head_index: The state of rotation, a circular index of where the sequence currently starts
        is_reflected: The state of reflection
    """

    def __init__(self, underlying, head_index: IndexO = 0, is_reflected: bool = False):
        """Initializes the instance with the sequence and the states."""
        self._kind = type(underlying) if isinstance(underlying, (list, tuple, str)) else list
        self.underlying = RingSeq(underlying)
        self.head_index = head_index
        self.is_reflected = is_reflected

    def __direction_multiplier(self) -> int:
        return 1 if self.is_reflected else -1

    def rotate_r(self, step: int = 1) -> None:
        """Updates the rotation state by some steps to the right.

        Examples:
          >>> r = Ring([1, 2, 3])
          >>> r.rotate_r(1)
          >>> r.current()
          [3, 1, 2]
        """
        self.head_index += step * self.__direction_multiplier()

    def rotate_l(self, step: int = 1) -> None:
        """Updates the rotation state by some steps to the left.

        Examples:
          >>> r = Ring([1, 2, 3])
          >>> r.rotate_l(1)
          >>> r.current()
          [2, 3, 1]
        """
        self.rotate_r(-step)

    def reflect(self) -> None:
        """Inverts the reflection state.

        Examples:
          >>> r = Ring([1, 2, 3])
          >>> r.reflect()
          >>> r.current()
          [1, 3, 2]
        """
        self.is_reflected = not self.is_reflected

    def current_head(self) -> Any:
        """Gets the start of the sequence at the current rotation state.

        Examples:
          >>> r = Ring([1, 2, 3])
          >>> r.rotate_r(1)
          >>> r.current_head()
          3
        """
        return self.underlying[self.head_index]

    def current(self):
        """Gets the sequence at the current rotation and reflection state,
        in the same concrete type as the original input.
        """
        ring = (
            self.underlying.reflect_at(self.head_index)
            if self.is_reflected
            else self.underlying.start_at(self.head_index)
        )
        if self._kind is str:
            return ring.to_str()
        if self._kind is tuple:
            return ring.to_tuple()
        return ring.to_list()
