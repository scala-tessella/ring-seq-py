"""Contains the `RingSeq` class.

Use `RingSeq` to enable dot notation.

Typical usage example:

  >>> RingSeq('ABC').rotate_left(1)
  'BCA'

  instead of

  >>> rotate_left('ABC', 1)
  'BCA'
"""
from ring_seq.methods import *


class RingSeq:
    """Wrapper class for circular methods.

    Use this class to enable dot notation.

    Attributes:
        underlying: The wrapped sequence.
    """

    def __init__(self, underlying: Seq):
        """Initializes the instance with the sequence."""
        self.underlying = underlying

    def index_from(self, i: IndexO) -> Index:
        """Normalizes a given circular index of a sequence.

        Examples:
          >>> RingSeq('ABC').index_from(-1)
          2
          >>> RingSeq('ABC').index_from(3)
          0

        Args:
          i: circular index

        Returns:
          A standard index

        Raises:
          ArithmeticError: An error occurs if the sequence is empty.
        """
        return index_from(self.underlying, i)

    def apply_o(self, i: IndexO) -> Any:
        """Gets the element at some circular index.

        Examples:
          >>> RingSeq('ABC').apply_o(-1)
          'C'
          >>> RingSeq('ABC').apply_o(3)
          'A'
          >>> 'ABC'[-1]
          'C'
          >>> 'ABC'[3] # doctest: +SKIP
          IndexError: string index out of range

        Notes:
          As shown in the examples, behaves differently from standard method `[i]`.

        Args:
          i: circular index

        Returns:
          The element at circular index
        """
        return apply_o(self.underlying, i)

    def rotate_right(self, step: int) -> Seq:
        """Rotates the sequence to the right by some steps.

        Examples:
          >>> RingSeq('ABC').rotate_right(1)
          'CAB'

        Args:
          step: number of rotation steps to the right

        Returns:
          The rotated sequence
        """
        return rotate_right(self.underlying, step)

    def rotate_left(self, step: int) -> Seq:
        """Rotates the sequence to the left by some steps.

        Examples:
          >>> RingSeq('ABC').rotate_left(1)
          'BCA'

        Args:
          step: number of rotation steps to the left

        Returns:
          The rotated sequence
        """
        return rotate_left(self.underlying, step)

    def start_at(self, i: IndexO) -> Seq:
        """Rotates the sequence to start at some circular index.

        Examples:
          >>> RingSeq('ABC').start_at(1)
          'BCA'

        Notes:
          Is equivalent to `rotate_left`.

        Args:
          i: circular index where the sequence starts

        Returns:
          The rotated sequence
        """
        return start_at(self.underlying, i)

    def reflect_at(self, i: IndexO = 0) -> Seq:
        """Reflects the sequence to start at some circular index.

        Examples:
          >>> RingSeq('ABC').reflect_at()
          'ACB'
          >>> RingSeq('ABC').reflect_at(1)
          'BAC'

        Notes:
          `reflect_at(-1)` is equivalent to `reversed`.

        Args:
          i: circular index where the reflected sequence starts

        Returns:
          The reflected sequence
        """
        return reflect_at(self.underlying, i)

    def slice_o(self, start: IndexO, end: IndexO, step: int = 1) -> Seq:
        """Selects an interval of elements.

        Examples:
          >>> RingSeq('ABC').slice_o(-1, 5)
          'CABCAB'
          >>> 'ABC'[-1:5]
          'C'
          >>> RingSeq('ABC').slice_o(-1, 5, 2)
          'CBA'
          >>> 'ABC'[-1:5:2]
          'C'

        Notes:
          Given the definition of circular sequence, a slice can contain more elements than the sequence itself.
          As shown in the examples, behaves differently from standard methods `[i:j]` and `[i:j:k]`.

        Args:
          start: circular index where the slice starts
          end: circular index where the slice ends
          step: number of steps for filtering

        Returns:
          The sliced sequence, with only the first element every each step

        Raises:
          ValueError: An error occurs if slice step is zero.
        """
        return slice_o(self.underlying, start, end, step)

    def rotations(self) -> Iterator[Seq]:
        """Computes all the rotations of this circular sequence

        Examples:
          >>> list(RingSeq('ABC').rotations())
          ['ABC', 'BCA', 'CAB']
          >>> list(RingSeq('').rotations())
          []

        Returns:
          The sequence and its rotations, 1 step at a time to the left
        """
        return rotations(self.underlying)

    def index_o(self, x: Any, start: IndexO = 0, end: IndexO = maxsize) -> Index:
        """Gets the index of the first occurrence of a sub-sequence.

        Examples:
          >>> RingSeq('ABC').index_o('B', 2, 7)
          1
          >>> 'ABC'.index('B', 2, 7) # doctest: +SKIP
          ValueError: substring not found
          >>> RingSeq('ABC').index_o('BCAB', 2, 8)
          1

        Notes:
          Given the definition of circular sequence, the searched slice can contain more elements than the sequence itself.
          As shown in the examples, behaves differently from standard method `index(x[, i[, j]])`.

        Args:
          x: sub-sequence to be found, can be a `str` or a single element from a `list` or from a `tuple`
          start: circular index where the search starts
          end: circular index where the search ends

        Returns:
          A standard index

        Raises:
          Value error: An error occurs if the sub-sequence is invalid or not found.
        """
        return index_o(self.underlying, x, start, end)

    def reflections(self) -> Iterator[Seq]:
        """Computes all the reflections of this circular sequence

        Examples:
          >>> list(RingSeq('ABC').reflections())
          ['ABC', 'ACB']
          >>> list(RingSeq('').reflections())
          []

        Returns:
          The sequence and its reflection
        """
        return reflections(self.underlying)

    def reversions(self) -> Iterator[Seq]:
        """Computes all the reversions of this circular sequence

        Examples:
          >>> list(RingSeq('ABC').reversions())
          ['ABC', 'CBA']
          >>> list(RingSeq('').reversions())
          []

        Returns:
          The sequence and its reversion
        """
        return reversions(self.underlying)

    def rotations_and_reflections(self) -> Iterator[Seq]:
        """Computes all the rotations and reflections of this circular sequence

        Examples:
          >>> list(RingSeq('ABC').rotations_and_reflections())
          ['ABC', 'BCA', 'CAB', 'ACB', 'CBA', 'BAC']
          >>> list(RingSeq('').rotations_and_reflections())
          []

        Returns:
          The sequence and its rotations, and their reflections
        """
        return rotations_and_reflections(self.underlying)

    def is_rotation_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a rotation of a given sequence.

        Examples:
          >>> RingSeq('ABC').is_rotation_of('BCA')
          True
          >>> RingSeq('ABC').is_rotation_of('ABC')
          True

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any rotation of that
        """
        return is_rotation_of(self.underlying, that)

    def is_reflection_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a reflection of a given sequence.

        Examples:
          >>> RingSeq('ABC').is_reflection_of('ACB')
          True
          >>> RingSeq('ABC').is_reflection_of('ABC')
          True

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any reflection of that
        """
        return is_reflection_of(self.underlying, that)

    def is_reversion_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a reversion of a given sequence.

        Examples:
          >>> RingSeq('ABC').is_reversion_of('CBA')
          True
          >>> RingSeq('ABC').is_reversion_of('ABC')
          True

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any reversion of that
        """
        return is_reversion_of(self.underlying, that)

    def is_rotation_or_reflection_of(self, that: Seq) -> bool:
        """Tests whether this circular sequence is a rotation and/or reflection of a given sequence.

        Examples:
          >>> RingSeq('ABC').is_rotation_or_reflection_of('BAC')
          True
          >>> RingSeq('ABC').is_rotation_or_reflection_of('ABC')
          True

        Args:
          that: sequence to be compared

        Returns:
          True if equal to any combination of rotation and reflection of that
        """
        return is_rotation_or_reflection_of(self.underlying, that)

    def rotational_symmetry(self) -> int:
        """Computes the order of rotational symmetry possessed by this circular sequence.

        Examples:
          >>> RingSeq('-|--|--|--|-').rotational_symmetry()
          4
          >>> RingSeq('-|+-|+-|+-|+').rotational_symmetry()
          4

        Returns:
          The rotational symmetry order, that is the number >= 1 of rotations
          in which a circular sequence looks exactly the same
        """
        return rotational_symmetry(self.underlying)

    def symmetry_indices(self) -> list[Index]:
        """Finds the indices of each element of this circular sequence close to an axis of reflectional symmetry.

        Examples:
          >>> RingSeq('-|--|--|--|-').symmetry_indices()
          [1, 4, 7, 10]
          >>> RingSeq('-|+-|+-|+-|+').symmetry_indices()
          []

        Returns:
          The indices of each element close to an axis of reflectional symmetry,
          that is a line of symmetry that splits the sequence in two identical halves
        """
        return symmetry_indices(self.underlying)

    def symmetry(self) -> int:
        """Computes the order of reflectional (mirror) symmetry possessed by this circular sequence.

        Examples:
          >>> RingSeq('-|--|--|--|-').symmetry()
          4
          >>> RingSeq('-|+-|+-|+-|+').symmetry()
          0

        Notes:
          Reflectional symmetry is always lower or equal than rotational symmetry.

        Returns:
          The reflectional (mirror) symmetry order, that is the number >= 0 of reflections
          in which a circular sequence looks exactly the same
        """
        return symmetry(self.underlying)
