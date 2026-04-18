"""Contains all the library methods plus new types.

They add new operations to `list`, `tuple` and `str`
(together represente by type `Seq`)
for when such a sequence needs to be considered **circular**,
its elements forming a ring.

Typical usage example:
  >>> rotate_left('ABC', 1)
  'BCA'
"""
from sys import maxsize
from dataclasses import dataclass
from itertools import chain, dropwhile, takewhile
from typing import Any, Callable, Iterator, Optional, TypeAlias, TypeVar
from math import ceil, fmod

# For improved readability, the index of a collection
Index: TypeAlias = int

# For improved readability, the circular index of a collection
IndexO: TypeAlias = int

# There are Sequence types, for example range, that is difficult to consider circular
Seq = TypeVar("Seq", list, str, tuple)


class AxisLocation:
    """A location on the circular sequence where a symmetry axis can pass through.

    - `Vertex`: the axis passes directly through the element at that index.
    - `Edge`: the axis passes between the elements at those two indices.
    """


@dataclass(frozen=True)
class Vertex(AxisLocation):
    """A symmetry axis location passing through a single element."""
    i: Index


@dataclass(frozen=True)
class Edge(AxisLocation):
    """A symmetry axis location passing between two adjacent elements."""
    i: Index
    j: Index


def index_from(ring: Seq, i: IndexO) -> Index:
    """Normalizes a given circular index of a sequence.

    Examples:
      >>> index_from('ABC', -1)
      2
      >>> index_from('ABC', 3)
      0

    Args:
      ring: a sequence
      i: circular index

    Returns:
      A standard index

    Raises:
      ArithmeticError: An error occurs if the sequence is empty.
    """
    length: int = len(ring)
    if length == 0:
        raise (ArithmeticError("An empty collection has no normalized index"))
    n: IndexO = int(fmod(i, length))
    if n < 0:
        return n + length
    else:
        return n


def apply_o(ring: Seq, i: IndexO) -> Any:
    """Gets the element at some circular index.

    Examples:
      >>> apply_o('ABC', -1)
      'C'
      >>> apply_o('ABC', 3)
      'A'
      >>> 'ABC'[-1]
      'C'
      >>> 'ABC'[3] # doctest: +SKIP
      IndexError: string index out of range

    Notes:
      As shown in the examples, behaves differently from standard method `[i]`.

    Args:
      ring: a sequence
      i: circular index

    Returns:
      The element at circular index
    """
    return ring[index_from(ring, i)]


def rotate_right(ring: Seq, step: int) -> Seq:
    """Rotates the sequence to the right by some steps.

    Examples:
      >>> rotate_right('ABC', 1)
      'CAB'

    Args:
      ring: a sequence
      step: number of rotation steps to the right

    Returns:
      The rotated sequence
    """
    j: Index = len(ring) - index_from(ring, step)
    return ring[j:] + ring[:j]


def rotate_left(ring: Seq, step: int) -> Seq:
    """Rotates the sequence to the left by some steps.

    Examples:
      >>> rotate_left('ABC', 1)
      'BCA'

    Args:
      ring: a sequence
      step: number of rotation steps to the left

    Returns:
      The rotated sequence
    """
    return rotate_right(ring, -step)


def start_at(ring: Seq, i: IndexO) -> Seq:
    """Rotates the sequence to start at some circular index.

    Examples:
      >>> start_at('ABC', 1)
      'BCA'

    Notes:
      Is equivalent to `rotate_left`.

    Args:
      ring: a sequence
      i: circular index where the sequence starts

    Returns:
      The rotated sequence
    """
    return rotate_left(ring, i)


def __typed_assemble(t: type, iterator: Iterator[Any]) -> Seq:
    if t is str:
        return "".join(iterator)
    elif t is list:
        return list(iterator)
    elif t is tuple:
        return tuple(iterator)
    else:
        raise (TypeError("Unexpected type, currently str, list and tuple checked"))


def __typed_reverse(ring: Seq) -> Seq:
    return __typed_assemble(type(ring), reversed(ring))


def reflect_at(ring: Seq, i: IndexO = 0) -> Seq:
    """Reflects the sequence to start at some circular index.

    Examples:
      >>> reflect_at('ABC')
      'ACB'
      >>> reflect_at('ABC', 1)
      'BAC'

    Notes:
      `reflect_at(-1)` is equivalent to `reversed`.

    Args:
      ring: a sequence
      i: circular index where the reflected sequence starts

    Returns:
      The reflected sequence
    """
    return __typed_reverse(start_at(ring, i + 1))


def slice_o(ring: Seq, start: IndexO, end: IndexO, step: int = 1) -> Seq:
    """Selects an interval of elements.

    Examples:
      >>> slice_o('ABC', -1, 5)
      'CABCAB'
      >>> 'ABC'[-1:5]
      'C'
      >>> slice_o('ABC', -1, 5, 2)
      'CBA'
      >>> 'ABC'[-1:5:2]
      'C'

    Notes:
      Given the definition of circular sequence, a slice can contain more elements than the sequence itself.
      As shown in the examples, behaves differently from standard methods `[i:j]` and `[i:j:k]`.

    Args:
      ring: a sequence
      start: circular index where the slice starts
      end: circular index where the slice ends
      step: number of steps for filtering

    Returns:
      The sliced sequence, with only the first element every each step

    Raises:
      ValueError: An error occurs if slice step is zero.
    """
    if step == 0:
        return ring[start:end:step]
    length: int = len(ring)
    if length == 0:
        return ring
    gap: int = end - start
    if gap < 0 or step < 0:
        return ring[:0]
    else:
        times: int = int(ceil(gap / length) + 1)
        all_elements: Seq = (start_at(ring, start) * times)[:gap]
        if step == 1:
            return all_elements
        else:
            filtered_indices: Iterator[Index] = filter(lambda i: i % step == 0, range(gap))
            filtered_elements: Iterator[Any] = map(lambda i: all_elements[i], filtered_indices)
            return __typed_assemble(type(ring), filtered_elements)


def index_o(ring: Seq, x: Any, start: IndexO = 0, end: IndexO = maxsize) -> Index:
    """Gets the index of the first occurrence of a sub-sequence.

    Examples:
      >>> index_o('ABC', 'B', 2, 7)
      1
      >>> 'ABC'.index('B', 2, 7) # doctest: +SKIP
      ValueError: substring not found
      >>> index_o('ABC', 'BCAB', 2, 8)
      1

    Notes:
      Given the definition of circular sequence, the searched slice can contain more elements than the sequence itself.
      As shown in the examples, behaves differently from standard method `index(x[, i[, j]])`.

    Args:
      ring: a sequence
      x: sub-sequence to be found, can be a `str` or a single element from a `list` or from a `tuple`
      start: circular index where the search starts
      end: circular index where the search ends

    Returns:
      A standard index

    Raises:
      Value error: An error occurs if the sub-sequence is invalid or not found.
    """
    length = len(ring)
    if length == 0:
        return ring.index(x)
    else:
        adjusted_to: int = min(end, start + length + len(x) - 1)
        s: Seq = slice_o(ring, start, adjusted_to)
        return index_from(ring, s.index(x) + start)


def take_while_o(ring: Seq, p: Callable[[Any], bool], from_: IndexO = 0) -> Seq:
    """Selects the longest prefix of elements starting at some circular index that satisfy a predicate.

    Examples:
      >>> take_while_o((0, 1, 2, 3, 4), lambda x: x < 3, 1)
      (1, 2)
      >>> take_while_o((0, 1, 2, 3, 4), lambda x: x != 1, 3)
      (3, 4, 0)

    Args:
      ring: a sequence
      p: the predicate used to test elements
      from_: circular index where the prefix starts

    Returns:
      The longest prefix from `from_` whose elements all satisfy `p`
    """
    if len(ring) == 0:
        return ring
    return __typed_assemble(type(ring), takewhile(p, start_at(ring, from_)))


def drop_while_o(ring: Seq, p: Callable[[Any], bool], from_: IndexO = 0) -> Seq:
    """Drops the longest prefix of elements starting at some circular index that satisfy a predicate.

    Examples:
      >>> drop_while_o((0, 1, 2, 3, 4), lambda x: x < 3, 1)
      (3, 4, 0)

    Args:
      ring: a sequence
      p: the predicate used to test elements
      from_: circular index where the prefix starts

    Returns:
      The suffix remaining after dropping the longest prefix from `from_` whose elements all satisfy `p`
    """
    if len(ring) == 0:
        return ring
    return __typed_assemble(type(ring), dropwhile(p, start_at(ring, from_)))


def span_o(ring: Seq, p: Callable[[Any], bool], from_: IndexO = 0) -> tuple[Seq, Seq]:
    """Splits this circular sequence into a prefix/suffix pair at the first element, starting from some
    circular index, that does not satisfy the predicate.

    Examples:
      >>> span_o((0, 1, 2, 3, 4), lambda x: x < 3, 1)
      ((1, 2), (3, 4, 0))

    Args:
      ring: a sequence
      p: the predicate used to test elements
      from_: circular index where the split starts

    Returns:
      A pair `(take_while_o(ring, p, from_), drop_while_o(ring, p, from_))`
    """
    return take_while_o(ring, p, from_), drop_while_o(ring, p, from_)


def __transformations(ring: Seq, f: Callable[[Seq], Iterator[Seq]]) -> Iterator[Seq]:
    if len(ring) == 0:
        return iter(ring)
    else:
        return f(ring)


def rotations(ring: Seq) -> Iterator[Seq]:
    """Computes all the rotations of this circular sequence

    Examples:
      >>> list(rotations('ABC'))
      ['ABC', 'BCA', 'CAB']
      >>> list(rotations(''))
      []

    Args:
      ring: a sequence

    Returns:
      The sequence and its rotations, 1 step at a time to the left
    """

    return __transformations(ring, lambda r: map(lambda stp: rotate_left(r, stp), range(len(r))))


def reflections(ring: Seq) -> Iterator[Seq]:
    """Computes all the reflections of this circular sequence

    Examples:
      >>> list(reflections('ABC'))
      ['ABC', 'ACB']
      >>> list(reflections(''))
      []

    Args:
      ring: a sequence

    Returns:
      The sequence and its reflection
    """
    return __transformations(ring, lambda r: iter([r, reflect_at(r, 0)]))


def reversions(ring: Seq) -> Iterator[Seq]:
    """Computes all the reversions of this circular sequence

    Examples:
      >>> list(reversions('ABC'))
      ['ABC', 'CBA']
      >>> list(reversions(''))
      []

    Args:
      ring: a sequence

    Returns:
      The sequence and its reversion
    """
    return __transformations(ring, lambda r: iter([r, __typed_reverse(r)]))


def __flatten(iterator_of_iterator: Iterator[Iterator[Any]]) -> Iterator[Any]:
    return chain.from_iterable(iterator_of_iterator)


def __flat_map(f: Callable[[Any], Iterator[Any]], iterator: Iterator[Any]) -> Iterator[Any]:
    return __flatten(map(f, iterator))


def grouped_o(ring: Seq, size: int) -> Iterator[Seq]:
    """Groups elements of this circular sequence in fixed-size blocks.

    Examples:
      >>> list(grouped_o('ABCDE', 2))
      ['AB', 'CD', 'EA', 'BC', 'DE']
      >>> list(grouped_o('', 2))
      []

    Args:
      ring: a sequence
      size: the number of elements per group

    Returns:
      An iterator of `len(ring)` groups of length `size`, or empty if the sequence is empty
    """
    n: int = len(ring)
    if n == 0:
        return iter([])
    return (slice_o(ring, i * size, i * size + size) for i in range(n))


def zip_with_index_o(ring: Seq, from_: IndexO = 0) -> Iterator[tuple[Any, Index]]:
    """Iterates over the elements paired with their original (circular) index, starting at some
    circular index.

    Examples:
      >>> list(zip_with_index_o(('a', 'b', 'c'), 1))
      [('b', 1), ('c', 2), ('a', 0)]
      >>> list(zip_with_index_o(('a', 'b', 'c')))
      [('a', 0), ('b', 1), ('c', 2)]
      >>> list(zip_with_index_o(()))
      []

    Args:
      ring: a sequence
      from_: circular index where the iteration starts

    Returns:
      An iterator of `(element, index)` pairs of length `len(ring)`, with indices in `[0, len(ring))`
    """
    n: int = len(ring)
    if n == 0:
        return iter([])
    start: Index = index_from(ring, from_)
    return ((x, (start + i) % n) for i, x in enumerate(start_at(ring, from_)))


def rotations_and_reflections(ring: Seq) -> Iterator[Seq]:
    """Computes all the rotations and reflections of this circular sequence

    Examples:
      >>> list(rotations_and_reflections('ABC'))
      ['ABC', 'BCA', 'CAB', 'ACB', 'CBA', 'BAC']
      >>> list(rotations_and_reflections(''))
      []

    Args:
      ring: a sequence

    Returns:
      The sequence and its rotations, and their reflections
    """
    return __transformations(ring, lambda r: __flat_map(rotations, reflections(r)))


def __is_transformation_of(ring: Seq, that: Seq, f: Callable[[Seq], Iterator[Seq]]) -> bool:
    return len(ring) == len(that) and that in f(ring)


def is_rotation_of(ring: Seq, that: Seq) -> bool:
    """Tests whether this circular sequence is a rotation of a given sequence.

    Examples:
      >>> is_rotation_of('ABC', 'BCA')
      True
      >>> is_rotation_of('ABC', 'ABC')
      True

    Args:
      ring: a sequence
      that: sequence to be compared

    Returns:
      True if equal to any rotation of that
    """
    return __is_transformation_of(ring, that, lambda r: rotations(r))


def is_reflection_of(ring: Seq, that: Seq) -> bool:
    """Tests whether this circular sequence is a reflection of a given sequence.

    Examples:
      >>> is_reflection_of('ABC', 'ACB')
      True
      >>> is_reflection_of('ABC', 'ABC')
      True

    Args:
      ring: a sequence
      that: sequence to be compared

    Returns:
      True if equal to any reflection of that
    """
    return __is_transformation_of(ring, that, lambda r: reflections(r))


def is_reversion_of(ring: Seq, that: Seq) -> bool:
    """Tests whether this circular sequence is a reversion of a given sequence.

    Examples:
      >>> is_reversion_of('ABC', 'CBA')
      True
      >>> is_reversion_of('ABC', 'ABC')
      True

    Args:
      ring: a sequence
      that: sequence to be compared

    Returns:
      True if equal to any reversion of that
    """
    return __is_transformation_of(ring, that, lambda r: reversions(r))


def is_rotation_or_reflection_of(ring: Seq, that: Seq) -> bool:
    """Tests whether this circular sequence is a rotation and/or reflection of a given sequence.

    Examples:
      >>> is_rotation_or_reflection_of('ABC', 'BAC')
      True
      >>> is_rotation_or_reflection_of('ABC', 'ABC')
      True

    Args:
      ring: a sequence
      that: sequence to be compared

    Returns:
      True if equal to any combination of rotation and reflection of that
    """
    return __is_transformation_of(ring, that, lambda r: rotations_and_reflections(r))


def align_to(ring: Seq, that: Seq) -> Optional[Index]:
    """Finds the rotation offset that aligns this circular sequence with a given sequence.

    Examples:
      >>> align_to((0, 1, 2), (2, 0, 1))
      2
      >>> align_to((0, 1, 2), (0, 1, 2))
      0
      >>> align_to((0, 1, 2), (1, 0, 2)) is None
      True
      >>> align_to((0, 1, 2), (0, 1)) is None
      True

    Args:
      ring: a sequence
      that: the sequence to align to

    Returns:
      The shift `k` such that `start_at(ring, k) == that`, or `None` if no rotation matches
    """
    if len(ring) != len(that):
        return None
    if len(ring) == 0:
        return 0
    for k in range(len(ring)):
        if start_at(ring, k) == that:
            return k
    return None


def hamming_distance(ring: Seq, that: Seq) -> int:
    """Counts the number of positions at which corresponding elements differ (Hamming distance).

    Examples:
      >>> hamming_distance((1, 0, 1, 1), (1, 1, 0, 1))
      2
      >>> hamming_distance((1, 2, 3), (1, 2, 3))
      0

    Args:
      ring: a sequence
      that: the sequence to compare against, must have the same size

    Returns:
      The count of positional mismatches

    Raises:
      ValueError: An error occurs if the sequences do not have the same size.
    """
    if len(ring) != len(that):
        raise ValueError("sequences must have the same size")
    return sum(1 for a, b in zip(ring, that) if a != b)


def min_rotational_hamming_distance(ring: Seq, that: Seq) -> int:
    """Computes the minimum Hamming distance over all rotations of this circular sequence.

    Examples:
      >>> min_rotational_hamming_distance((1, 2, 3, 4), (3, 4, 1, 2))
      0
      >>> min_rotational_hamming_distance((0, 0, 1, 1, 0), (1, 1, 0, 0, 1))
      1

    Args:
      ring: a sequence
      that: the sequence to compare against, must have the same size

    Returns:
      `0` iff `that` is a rotation of `ring`, otherwise the smallest number of positional mismatches
      over any rotation

    Raises:
      ValueError: An error occurs if the sequences do not have the same size.
    """
    if len(ring) != len(that):
        raise ValueError("sequences must have the same size")
    if len(ring) == 0:
        return 0
    return min(hamming_distance(rotation, that) for rotation in rotations(ring))


def __are_folds_symmetrical(ring: Seq, n: int) -> bool:
    return rotate_right(ring, int(len(ring) / n)) == ring


def rotational_symmetry(ring: Seq) -> int:
    """Computes the order of rotational symmetry possessed by this circular sequence.

    Examples:
      >>> rotational_symmetry('-|--|--|--|-')
      4
      >>> rotational_symmetry('-|+-|+-|+-|+')
      4

    Args:
      ring: a sequence

    Returns:
      The rotational symmetry order, that is the number >= 1 of rotations
      in which a circular sequence looks exactly the same
    """
    length: int = len(ring)
    if length < 2:
        return 1
    else:
        divisors_in_decreasing_size: range = range(int(length / 2), 2, -1)
        exact_divisors: Iterator[int] = filter(lambda divisor: length % divisor == 0, divisors_in_decreasing_size)
        folds_in_decreasing_size: Iterator[int] = iter([length] + list(exact_divisors))
        symmetric_folds: Iterator[int] = filter(lambda fs: __are_folds_symmetrical(ring, fs), folds_in_decreasing_size)
        return next(symmetric_folds, 1)


def symmetry_indices(ring: Seq) -> list[Index]:
    """Finds the shifts at which this circular sequence equals its reversal rotated left.

    Each returned shift identifies one axis of reflectional symmetry.

    Examples:
      >>> symmetry_indices('-|--|--|--|-')
      [0, 3, 6, 9]
      >>> symmetry_indices('-|+-|+-|+-|+')
      []

    Args:
      ring: a sequence

    Returns:
      The shifts `s` such that `ring == rotate_left(reversed(ring), s)`,
      one per axis of reflectional symmetry
    """
    if len(ring) == 0:
        return []
    reversed_ring: Seq = __typed_reverse(ring)
    return [shift for shift in range(len(ring)) if ring == rotate_left(reversed_ring, shift)]


def reflectional_symmetry_axes(ring: Seq) -> list[tuple[AxisLocation, AxisLocation]]:
    """Calculates the axes of reflectional symmetry.

    Each axis is returned as a pair of `AxisLocation` values: the two points on the
    cycle where the axis passes.

    Examples:
      >>> reflectional_symmetry_axes((1, 1, 2, 3, 2))
      [(Vertex(i=3), Edge(i=0, j=1))]
      >>> reflectional_symmetry_axes('ABC')
      []

    Args:
      ring: a sequence

    Returns:
      A list where each pair represents the two points on the cycle where an axis passes
    """
    n: int = len(ring)

    def edge_indices(i: Index) -> Edge:
        return Edge(i, (i + 1) % n)

    def opposite_edge_index(i: Index) -> Index:
        return (i + n // 2) % n

    axes: list[tuple[AxisLocation, AxisLocation]] = []
    for shift in symmetry_indices(ring):
        # The reflection maps index i to (n - 1 - shift - i) % n.
        # Fixed points satisfy 2*i == n - 1 - shift (mod n). Let K = n - 1 - shift.
        effective_k: int = (n - 1 - shift) % n
        if n % 2 != 0:
            # Odd n: 2*i = K (mod n) has exactly one vertex solution.
            # Inverse of 2 mod n is (n + 1) / 2.
            v: Index = (effective_k * ((n + 1) // 2)) % n
            axes.append((Vertex(v), edge_indices(opposite_edge_index(v))))
        elif effective_k % 2 == 0:
            # Even n, even K: two opposite vertex solutions.
            v1: Index = effective_k // 2
            axes.append((Vertex(v1), Vertex(opposite_edge_index(v1))))
        else:
            # Even n, odd K: axis passes through two opposite edges.
            e1: Index = (effective_k - 1) // 2
            axes.append((edge_indices(e1), edge_indices(opposite_edge_index(e1))))
    return axes


def symmetry(ring: Seq) -> int:
    """Computes the order of reflectional (mirror) symmetry possessed by this circular sequence.

    Examples:
      >>> symmetry('-|--|--|--|-')
      4
      >>> symmetry('-|+-|+-|+-|+')
      0

    Notes:
      Reflectional symmetry is always lower or equal than rotational symmetry.

    Args:
      ring: a sequence

    Returns:
      The reflectional (mirror) symmetry order, that is the number >= 0 of reflections
      in which a circular sequence looks exactly the same
    """
    return len(symmetry_indices(ring))


def __least_rotation_booth(ring: Seq) -> Index:
    n: int = len(ring)
    total: int = 2 * n
    f: list[int] = [-1] * total
    k: int = 0
    j: int = 1
    while j < total:
        sj: Any = ring[j % n]
        i: int = f[j - k - 1]
        while i != -1 and sj != ring[(k + i + 1) % n]:
            if sj < ring[(k + i + 1) % n]:
                k = j - i - 1
            i = f[i]
        if i == -1 and sj != ring[(k + i + 1) % n]:
            if sj < ring[(k + i + 1) % n]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
        j += 1
    return k


def canonical_index(ring: Seq) -> Index:
    """Finds the starting index of the lexicographically smallest rotation (Booth's algorithm, O(n)).

    Examples:
      >>> canonical_index((2, 0, 1))
      1
      >>> canonical_index('CAB')
      1
      >>> canonical_index(())
      0

    Args:
      ring: a sequence whose elements are totally ordered

    Returns:
      The index `k` in `[0, len(ring))` such that `start_at(ring, k)` is the lex-smallest of all
      rotations; `0` for empty or single-element sequences
    """
    if len(ring) <= 1:
        return 0
    return __least_rotation_booth(ring)


def canonical(ring: Seq) -> Seq:
    """Returns the lexicographically smallest rotation of this circular sequence (necklace canonical form).

    Two circular sequences are rotations of each other iff their canonical forms are equal,
    making this useful for hashing or deduplicating equivalent rings.

    Examples:
      >>> canonical((2, 0, 1))
      (0, 1, 2)
      >>> canonical('CAB')
      'ABC'

    Args:
      ring: a sequence whose elements are totally ordered

    Returns:
      The lex-smallest rotation of `ring`
    """
    if len(ring) == 0:
        return ring
    return start_at(ring, canonical_index(ring))


def bracelet(ring: Seq) -> Seq:
    """Returns the lexicographically smallest representative under both rotation and reflection
    (bracelet canonical form).

    Two circular sequences belong to the same bracelet equivalence class iff their bracelet forms
    are equal, useful when mirror images are considered identical.

    Examples:
      >>> bracelet((2, 0, 1))
      (0, 1, 2)
      >>> bracelet('CBA')
      'ABC'

    Args:
      ring: a sequence whose elements are totally ordered

    Returns:
      The smaller of `canonical(ring)` and `canonical(reflect_at(ring))` by lexicographic ordering
    """
    if len(ring) == 0:
        return ring
    a: Seq = canonical(ring)
    b: Seq = canonical(reflect_at(ring))
    return a if a <= b else b
