"""Contains the RingSeq class.

Use RingSeq to enable dot notation.

Typical usage example:

  >>> RingSeq([0, 1, 2]).rotate_left(1)
  [1, 2, 0]

  instead of

  >>> rotate_left([0, 1, 2], 1)
  [1, 2, 0]
"""
from ring_seq.methods import *


class RingSeq:
    """Wrapper class for circular methods.

    Use RingSeq to enable dot notation.

    Attributes:
        underlying: The wrapped sequence.
    """

    def __init__(self, underlying: Seq):
        """Initializes the instance with the sequence.

        Args:
          underlying: The wrapped sequence.
        """
        self.underlying = underlying

    def index_from(self, i: IndexO) -> Index:
        """Normalizes a given circular index of a Seq.

        Examples:
          >>> RingSeq("ABC").index_from(-1)
          2
          >>> RingSeq("ABC").index_from(3)
          0

        Args:
          i: circular index

        Returns:
          A standard index
        """
        return index_from(self.underlying, i)

    def apply_o(self, i: IndexO) -> Any:
        """Gets the element at some circular index.

        Examples:
          >>> RingSeq("ABC").apply_o(-1)
          'C'
          >>> RingSeq("ABC").apply_o(3)
          'A'

        Args:
          i: circular index

        Returns:
          The element at circular index
        """
        return apply_o(self.underlying, i)

    def rotate_right(self, step: IndexO) -> Seq:
        """Rotates the sequence to the right by some steps.

        Examples:
          >>> RingSeq([3, 4, 5]).rotate_right(1)
          [5, 3, 4]

        Args:
          step: number of rotation steps to the right

        Returns:
          The rotated sequence
        """
        return rotate_right(self.underlying, step)

    def rotate_left(self, step: IndexO) -> Seq:
        """Rotates the sequence to the left by some steps.

        Examples:
          >>> RingSeq([3, 4, 5]).rotate_left(1)
          [4, 5, 3]

        Args:
          step: number of rotation steps to the left

        Returns:
          The rotated sequence
        """
        return rotate_left(self.underlying, step)

    def start_at(self, i: IndexO) -> Seq:
        """Rotates the sequence to start at some circular index.

        Examples:
          >>> RingSeq([3, 4, 5]).start_at(1)
          [4, 5, 3]

        Args:
          i: circular index where the sequence starts

        Returns:
          The rotated sequence
        """
        return start_at(self.underlying, i)

    def reflect_at(self, i: IndexO = 0) -> Seq:
        """Reflects the sequence to start at some circular index.

        Examples:
          >>> RingSeq([3, 4, 5]).reflect_at()
          [3, 5, 4]
          >>> RingSeq([3, 4, 5]).reflect_at(1)
          [4, 3, 5]

        Args:
          i: circular index where the reflected sequence starts

        Returns:
          The reflected sequence
        """
        return reflect_at(self.underlying, i)

    def slice_o(self, frm: IndexO, to: IndexO) -> Seq:
        """Selects an interval of elements.

        Args:
          frm: circular index where the slice starts
          to: circular index where the slice ends

        Returns:
          The sliced sequence
        """
        return slice_o(self.underlying, frm, to)

    def rotations(self) -> Iterator[Seq]:
        """Computes all the rotations of this circular sequence

        Returns:
          The sequence and its rotations, 1 step at a time to the right
        """
        return rotations(self.underlying)

    def reflections(self) -> Iterator[Seq]:
        """Computes all the reflections of this circular sequence

        Returns:
          The sequence and its reflection
        """
        return reflections(self.underlying)

    def reversions(self) -> Iterator[Seq]:
        """Computes all the reversions of this circular sequence

        Returns:
          The sequence and its reversion
        """
        return reversions(self.underlying)

    def rotations_and_reflections(self) -> Iterator[Seq]:
        """Computes all the rotations and reflections of this circular sequence

        Returns:
          The sequence and its rotations, and their reflections
        """
        return rotations_and_reflections(self.underlying)

    def is_rotation_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a rotation of a given sequence.

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any rotation of that
        """
        return is_rotation_of(self.underlying, that)

    def is_reflection_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a reflection of a given sequence.

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any reflection of that
        """
        return is_reflection_of(self.underlying, that)

    def is_reversion_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a reversion of a given sequence.

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any reversion of that
        """
        return is_reversion_of(self.underlying, that)

    def is_rotation_or_reflection_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a rotation and/or reflection of a given sequence.

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any combination of rotation and reflection of that
        """
        return is_rotation_or_reflection_of(self.underlying, that)

    def rotational_symmetry(self) -> int:
        """Computes the order of rotational symmetry possessed by this circular sequence.

        Returns:
          The rotational symmetry order
        """
        return rotational_symmetry(self.underlying)

    def symmetry_indices(self) -> list[Index]:
        """Finds the indices of each element of this circular sequence close to an axis of reflectional symmetry.

        Returns:
          The indices of the elements by which the reflectional symmetry axis are near
        """
        return symmetry_indices(self.underlying)

    def symmetry(self) -> int:
        """Computes the order of reflectional (mirror) symmetry possessed by this circular sequence.

        Returns:
          The reflectional (mirror) symmetry order
        """
        return symmetry(self.underlying)
