"""Contains the example Ring class.

Usage example:

  >>> r = Ring('ABC')
  >>> r.rotate_l(1)
  >>> r.current()
  'BCA'
"""
from ring_seq.methods import *


class Ring:
    """Wraps a sequence and keeps mutable states of rotation and reflection.

    Attributes:
        underlying: The wrapped sequence.
        head_index: The state of rotation, a circular index of where the sequence currently starts, default = 0
        is_reflected: The state of reflection
    """
    def __init__(self, underlying: Seq, head_index: IndexO = 0, is_reflected: bool = False):
        """Initializes the instance with the sequence and the states."""
        self.underlying = underlying
        self.head_index = head_index
        self.is_reflected = is_reflected

    def __direction_multiplier(self) -> int:
        if self.is_reflected:
            return 1
        else:
            return -1

    def rotate_r(self, step: int = 1):
        """Updates the rotation state by some steps to the right.

        Examples:
          >>> r = Ring('ABC')
          >>> r.rotate_r(1)
          >>> r.current()
          'CAB'

        Args:
          step: number of rotation steps to the right
        """
        self.head_index += step * self.__direction_multiplier()

    def rotate_l(self, step: int = 1):
        """Updates the rotation state by some steps to the left.

        Examples:
          >>> r = Ring('ABC')
          >>> r.rotate_l(1)
          >>> r.current()
          'BCA'

        Args:
          step: number of rotation steps to the left
        """
        self.rotate_r(-step)

    def reflect(self):
        """Inverts the reflection state.

        Examples:
          >>> r = Ring('ABC')
          >>> r.reflect()
          >>> r.current()
          'ACB'
        """
        self.is_reflected = not self.is_reflected

    def current_head(self) -> Any:
        """Gets the start of the sequence at the current rotation state.

        Examples:
          >>> r = Ring('ABC')
          >>> r.rotate_r(1)
          >>> r.current_head()
          'C'

        Returns:
          The current head element of the sequence
        """
        return apply_o(self.underlying, self.head_index)

    def current(self) -> Seq:
        """Gets the sequence at the current rotation and reflection state.

        Examples:
          >>> r = Ring('ABC')
          >>> r.rotate_r(1)
          >>> r.current()
          'CAB'

        Returns:
          The current sequence
        """
        if self.is_reflected:
            return reflect_at(self.underlying, self.head_index)
        else:
            return start_at(self.underlying, self.head_index)
