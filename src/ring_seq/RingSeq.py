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

    def take_while_o(self, p: Callable[[Any], bool], from_: IndexO = 0) -> Seq:
        """Selects the longest prefix of elements starting at some circular index that satisfy a predicate.

        Examples:
          >>> RingSeq((0, 1, 2, 3, 4)).take_while_o(lambda x: x < 3, 1)
          (1, 2)

        Args:
          p: the predicate used to test elements
          from_: circular index where the prefix starts

        Returns:
          The longest prefix from `from_` whose elements all satisfy `p`
        """
        return take_while_o(self.underlying, p, from_)

    def drop_while_o(self, p: Callable[[Any], bool], from_: IndexO = 0) -> Seq:
        """Drops the longest prefix of elements starting at some circular index that satisfy a predicate.

        Examples:
          >>> RingSeq((0, 1, 2, 3, 4)).drop_while_o(lambda x: x < 3, 1)
          (3, 4, 0)

        Args:
          p: the predicate used to test elements
          from_: circular index where the prefix starts

        Returns:
          The suffix remaining after dropping the longest prefix from `from_` whose elements all satisfy `p`
        """
        return drop_while_o(self.underlying, p, from_)

    def span_o(self, p: Callable[[Any], bool], from_: IndexO = 0) -> tuple[Seq, Seq]:
        """Splits this circular sequence into a prefix/suffix pair at the first element, starting from some
        circular index, that does not satisfy the predicate.

        Examples:
          >>> RingSeq((0, 1, 2, 3, 4)).span_o(lambda x: x < 3, 1)
          ((1, 2), (3, 4, 0))

        Args:
          p: the predicate used to test elements
          from_: circular index where the split starts

        Returns:
          A pair `(take_while_o(p, from_), drop_while_o(p, from_))`
        """
        return span_o(self.underlying, p, from_)

    def grouped_o(self, size: int) -> Iterator[Seq]:
        """Groups elements of this circular sequence in fixed-size blocks.

        Examples:
          >>> list(RingSeq('ABCDE').grouped_o(2))
          ['AB', 'CD', 'EA', 'BC', 'DE']

        Args:
          size: the number of elements per group

        Returns:
          An iterator of `len(ring)` groups of length `size`, or empty if the sequence is empty
        """
        return grouped_o(self.underlying, size)

    def zip_with_index_o(self, from_: IndexO = 0) -> Iterator[tuple[Any, Index]]:
        """Iterates over the elements paired with their original (circular) index, starting at some
        circular index.

        Examples:
          >>> list(RingSeq(('a', 'b', 'c')).zip_with_index_o(1))
          [('b', 1), ('c', 2), ('a', 0)]

        Args:
          from_: circular index where the iteration starts

        Returns:
          An iterator of `(element, index)` pairs of length `len(ring)`
        """
        return zip_with_index_o(self.underlying, from_)

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

    def align_to(self, that: Seq) -> Optional[Index]:
        """Finds the rotation offset that aligns this circular sequence with a given sequence.

        Examples:
          >>> RingSeq((0, 1, 2)).align_to((2, 0, 1))
          2
          >>> RingSeq((0, 1, 2)).align_to((1, 0, 2)) is None
          True

        Args:
          that: the sequence to align to

        Returns:
          The shift `k` such that `start_at(k) == that`, or `None` if no rotation matches
        """
        return align_to(self.underlying, that)

    def hamming_distance(self, that: Seq) -> int:
        """Counts the number of positions at which corresponding elements differ (Hamming distance).

        Examples:
          >>> RingSeq((1, 0, 1, 1)).hamming_distance((1, 1, 0, 1))
          2

        Args:
          that: the sequence to compare against, must have the same size

        Returns:
          The count of positional mismatches

        Raises:
          ValueError: An error occurs if the sequences do not have the same size.
        """
        return hamming_distance(self.underlying, that)

    def min_rotational_hamming_distance(self, that: Seq) -> int:
        """Computes the minimum Hamming distance over all rotations of this circular sequence.

        Examples:
          >>> RingSeq((1, 2, 3, 4)).min_rotational_hamming_distance((3, 4, 1, 2))
          0

        Args:
          that: the sequence to compare against, must have the same size

        Returns:
          `0` iff `that` is a rotation of this sequence, otherwise the smallest number of positional
          mismatches over any rotation

        Raises:
          ValueError: An error occurs if the sequences do not have the same size.
        """
        return min_rotational_hamming_distance(self.underlying, that)

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
        """Finds the shifts at which this circular sequence equals its reversal rotated left.

        Examples:
          >>> RingSeq('-|--|--|--|-').symmetry_indices()
          [0, 3, 6, 9]
          >>> RingSeq('-|+-|+-|+-|+').symmetry_indices()
          []

        Returns:
          The shifts `s` such that `ring == rotate_left(reversed(ring), s)`,
          one per axis of reflectional symmetry
        """
        return symmetry_indices(self.underlying)

    def reflectional_symmetry_axes(self) -> list[tuple[AxisLocation, AxisLocation]]:
        """Calculates the axes of reflectional symmetry.

        Examples:
          >>> RingSeq((1, 1, 2, 3, 2)).reflectional_symmetry_axes()
          [(Vertex(i=3), Edge(i=0, j=1))]
          >>> RingSeq('ABC').reflectional_symmetry_axes()
          []

        Returns:
          A list where each pair represents the two points on the cycle where an axis passes
        """
        return reflectional_symmetry_axes(self.underlying)

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

    def canonical_index(self) -> Index:
        """Finds the starting index of the lexicographically smallest rotation (Booth's algorithm, O(n)).

        Examples:
          >>> RingSeq((2, 0, 1)).canonical_index()
          1
          >>> RingSeq('CAB').canonical_index()
          1

        Returns:
          The index `k` in `[0, len(ring))` such that `start_at(k)` is the lex-smallest of all rotations
        """
        return canonical_index(self.underlying)

    def canonical(self) -> Seq:
        """Returns the lexicographically smallest rotation of this circular sequence
        (necklace canonical form).

        Examples:
          >>> RingSeq((2, 0, 1)).canonical()
          (0, 1, 2)
          >>> RingSeq('CAB').canonical()
          'ABC'

        Returns:
          The lex-smallest rotation of the sequence
        """
        return canonical(self.underlying)

    def bracelet(self) -> Seq:
        """Returns the lexicographically smallest representative under both rotation and reflection
        (bracelet canonical form).

        Examples:
          >>> RingSeq((2, 0, 1)).bracelet()
          (0, 1, 2)
          >>> RingSeq('CBA').bracelet()
          'ABC'

        Returns:
          The smaller of `canonical()` and `canonical(reflect_at(...))` by lexicographic ordering
        """
        return bracelet(self.underlying)
