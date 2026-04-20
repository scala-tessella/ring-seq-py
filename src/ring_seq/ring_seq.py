"""RingSeq — a Pythonic class for sequences considered circular.

A `RingSeq[T]` wraps any iterable of `T`, storing it internally as an
immutable tuple. Built-in sequence operations (`len`, indexing, slicing,
iteration, containment, equality, hashing) are implemented circularly.

Typical usage:

    >>> from ring_seq import RingSeq
    >>> RingSeq("RING").rotate_left(1).to_str()
    'INGR'
    >>> RingSeq([0, 1, 2, 3])[-1]
    3
    >>> RingSeq("ABC")[-1:5].to_str()
    'CABCAB'

Equality is positional and is agnostic to the input iterable kind used
at construction:

    >>> RingSeq("ABC") == RingSeq(["A", "B", "C"])
    True
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Sequence
from dataclasses import dataclass
from itertools import dropwhile, takewhile
from math import ceil
from typing import Generic, TypeAlias, TypeVar, overload

Index: TypeAlias = int
"""Standard (non-circular) index, in `[0, len)`."""

IndexO: TypeAlias = int
"""Circular index; any integer, normalized modulo the ring size."""

T = TypeVar("T")


class AxisLocation:
    """A location on the circular sequence where a symmetry axis can pass through.

    - `Vertex`: the axis passes directly through the element at that index.
    - `Edge`: the axis passes between the elements at those two indices.
    """


@dataclass(frozen=True)
class Vertex(AxisLocation):
    """A symmetry axis location passing through a single element."""

    i: Index


class Edge(AxisLocation):
    """A symmetry axis location passing between two consecutive elements of a circular sequence.

    The invariant `j == (i + 1) % n` is enforced at construction. Pattern matching
    with `match e: case Edge(i, j): ...` still works.
    """

    __match_args__ = ("i", "j")

    def __init__(self, i: Index, n: int):
        """Builds the edge starting at circular index `i` in a ring of size `n`.

        Args:
          i: circular index of the first endpoint (any integer, normalized to `[0, n)`)
          n: the ring size; must be positive

        Raises:
          ValueError: if `n <= 0`
        """
        if n <= 0:
            raise ValueError("ring size must be positive")
        self.i = i % n
        self.j = (self.i + 1) % n

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Edge) and self.i == other.i and self.j == other.j

    def __hash__(self) -> int:
        return hash((Edge, self.i, self.j))

    def __repr__(self) -> str:
        return f"Edge(i={self.i}, j={self.j})"


def _least_rotation_booth(s: tuple) -> Index:
    """Booth's O(n) algorithm: starting index of the lexicographically smallest rotation."""
    n = len(s)
    total = 2 * n
    f = [-1] * total
    k = 0
    j = 1
    while j < total:
        sj = s[j % n]
        i = f[j - k - 1]
        while i != -1 and sj != s[(k + i + 1) % n]:
            if sj < s[(k + i + 1) % n]:
                k = j - i - 1
            i = f[i]
        if i == -1 and sj != s[(k + i + 1) % n]:
            if sj < s[(k + i + 1) % n]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
        j += 1
    return k


class RingSeq(Generic[T], Sequence[T]):
    """A sequence considered circular, with ring-specific operations.

    The ring is stored internally as a tuple. Use `to_list()`, `to_tuple()`,
    or `to_str()` to unwrap at the boundary. All transformations return a new
    `RingSeq`; `RingSeq` instances are immutable and hashable.
    """

    __slots__ = ("_seq",)

    def __init__(self, seq: Iterable[T] = ()):
        """Builds a `RingSeq` from any iterable (empty by default)."""
        self._seq: tuple[T, ...] = tuple(seq)

    # ----- Python sequence protocol (circular) -----

    def __len__(self) -> int:
        return len(self._seq)

    @overload
    def __getitem__(self, i: int) -> T: ...
    @overload
    def __getitem__(self, i: slice) -> RingSeq[T]: ...
    def __getitem__(self, i):
        """Circular indexing and slicing.

        Any integer index wraps around the ring. A slice returns a `RingSeq` that
        may contain more elements than the original — cycling through the ring as
        needed. Negative step or reversed bounds produce an empty `RingSeq`.

        Examples:
          >>> RingSeq("ABC")[-1]
          'C'
          >>> RingSeq("ABC")[30001]
          'B'
          >>> RingSeq("ABC")[-1:5].to_str()
          'CABCAB'
          >>> RingSeq("ABC")[1:3].to_str()
          'BC'
          >>> RingSeq("ABCDE")[0:5:2].to_str()
          'ACE'
        """
        n = len(self._seq)
        if isinstance(i, slice):
            if n == 0:
                return RingSeq()
            start = 0 if i.start is None else i.start
            end = n if i.stop is None else i.stop
            step = 1 if i.step is None else i.step
            return self._circular_slice(start, end, step)
        if n == 0:
            raise IndexError("RingSeq index out of range")
        return self._seq[i % n]

    def __iter__(self) -> Iterator[T]:
        return iter(self._seq)

    def __contains__(self, x: object) -> bool:
        return x in self._seq

    def __eq__(self, other: object) -> bool:
        if isinstance(other, RingSeq):
            return self._seq == other._seq
        return NotImplemented

    def __lt__(self, other: RingSeq[T]) -> bool:
        if isinstance(other, RingSeq):
            return self._seq < other._seq
        return NotImplemented

    def __le__(self, other: RingSeq[T]) -> bool:
        if isinstance(other, RingSeq):
            return self._seq <= other._seq
        return NotImplemented

    def __hash__(self) -> int:
        return hash((RingSeq, self._seq))

    def __repr__(self) -> str:
        return f"RingSeq({self._seq!r})"

    # ----- Unwrap -----

    def to_list(self) -> list[T]:
        """Returns the ring as a new list.

        Examples:
          >>> RingSeq("ABC").to_list()
          ['A', 'B', 'C']
        """
        return list(self._seq)

    def to_tuple(self) -> tuple[T, ...]:
        """Returns the ring as a tuple (the internal storage).

        Examples:
          >>> RingSeq([1, 2, 3]).to_tuple()
          (1, 2, 3)
        """
        return self._seq

    def to_str(self, sep: str = "") -> str:
        """Joins the elements into a string using `sep`.

        Examples:
          >>> RingSeq("ABC").to_str()
          'ABC'
          >>> RingSeq([1, 2, 3]).to_str("-")
          '1-2-3'
        """
        return sep.join(str(x) for x in self._seq)

    # ----- Indexing helper -----

    def index_from(self, i: IndexO) -> Index:
        """Normalizes a circular index to `[0, len(self))`.

        Examples:
          >>> RingSeq("ABC").index_from(-1)
          2
          >>> RingSeq("ABC").index_from(3)
          0

        Raises:
          ArithmeticError: if the ring is empty.
        """
        n = len(self._seq)
        if n == 0:
            raise ArithmeticError("An empty collection has no normalized index")
        return i % n

    # ----- Rotation & reflection -----

    def rotate_right(self, step: int) -> RingSeq[T]:
        """Rotates the sequence right by `step` positions.

        Examples:
          >>> RingSeq("ABC").rotate_right(1).to_str()
          'CAB'
        """
        n = len(self._seq)
        if n == 0:
            return self
        j = n - (step % n)
        return RingSeq(self._seq[j:] + self._seq[:j])

    def rotate_left(self, step: int) -> RingSeq[T]:
        """Rotates the sequence left by `step` positions.

        Examples:
          >>> RingSeq("ABC").rotate_left(1).to_str()
          'BCA'
        """
        return self.rotate_right(-step)

    def start_at(self, i: IndexO) -> RingSeq[T]:
        """Rotates the sequence to start at circular index `i` (equivalent to `rotate_left(i)`).

        Examples:
          >>> RingSeq("ABC").start_at(1).to_str()
          'BCA'
        """
        return self.rotate_left(i)

    def reflect_at(self, i: IndexO = 0) -> RingSeq[T]:
        """Reflects the sequence with element at circular index `i` as the axis head.

        Examples:
          >>> RingSeq("ABC").reflect_at().to_str()
          'ACB'
          >>> RingSeq("ABC").reflect_at(1).to_str()
          'BAC'
        """
        rotated = self.start_at(i + 1)._seq
        return RingSeq(reversed(rotated))

    # ----- Circular slice internal helper -----

    def _circular_slice(self, start: IndexO, end: IndexO, step: int = 1) -> RingSeq[T]:
        if step == 0:
            raise ValueError("slice step cannot be zero")
        n = len(self._seq)
        if n == 0:
            return RingSeq()
        gap = end - start
        if gap < 0 or step < 0:
            return RingSeq()
        times = int(ceil(gap / n) + 1)
        rotated = self.start_at(start)._seq
        all_elements = (rotated * times)[:gap]
        if step == 1:
            return RingSeq(all_elements)
        return RingSeq(all_elements[::step])

    # ----- Lookup -----

    def index(self, value: T, start: IndexO = 0, stop: IndexO | None = None) -> Index:
        """Circular index of the first occurrence of `value`.

        Searches one full revolution by default. Searching past the end wraps around.

        Examples:
          >>> RingSeq("ABCA").index("A")
          0
          >>> RingSeq("ABCA").index("A", 1)
          3
          >>> RingSeq("ABC").index("A", 5)
          0

        Raises:
          ValueError: if `value` is not found.
        """
        n = len(self._seq)
        if n == 0:
            raise ValueError(f"{value!r} is not in RingSeq")
        limit = start + n if stop is None else min(stop, start + n)
        for k in range(start, limit):
            if self._seq[k % n] == value:
                return k % n
        raise ValueError(f"{value!r} is not in RingSeq")

    # ----- Slicing primitives -----

    def take_while(self, p: Callable[[T], bool], from_: IndexO = 0) -> RingSeq[T]:
        """Longest prefix from circular index `from_` whose elements satisfy `p`.

        Examples:
          >>> RingSeq((0, 1, 2, 3, 4)).take_while(lambda x: x < 3, 1).to_tuple()
          (1, 2)
          >>> RingSeq((0, 1, 2, 3, 4)).take_while(lambda x: x != 1, 3).to_tuple()
          (3, 4, 0)
        """
        if len(self._seq) == 0:
            return self
        return RingSeq(takewhile(p, self.start_at(from_)._seq))

    def drop_while(self, p: Callable[[T], bool], from_: IndexO = 0) -> RingSeq[T]:
        """Suffix after dropping the longest prefix from `from_` whose elements satisfy `p`.

        Examples:
          >>> RingSeq((0, 1, 2, 3, 4)).drop_while(lambda x: x < 3, 1).to_tuple()
          (3, 4, 0)
        """
        if len(self._seq) == 0:
            return self
        return RingSeq(dropwhile(p, self.start_at(from_)._seq))

    def span(self, p: Callable[[T], bool], from_: IndexO = 0) -> tuple[RingSeq[T], RingSeq[T]]:
        """Splits at the first element, starting at `from_`, that does not satisfy `p`.

        Examples:
          >>> take, drop = RingSeq((0, 1, 2, 3, 4)).span(lambda x: x < 3, 1)
          >>> take.to_tuple(), drop.to_tuple()
          ((1, 2), (3, 4, 0))
        """
        return self.take_while(p, from_), self.drop_while(p, from_)

    # ----- Iterators over rings -----

    def rotations(self) -> Iterator[RingSeq[T]]:
        """All rotations of this ring, one step at a time to the left.

        Examples:
          >>> [r.to_str() for r in RingSeq("ABC").rotations()]
          ['ABC', 'BCA', 'CAB']
        """
        if len(self._seq) == 0:
            return iter(())
        return (self.rotate_left(k) for k in range(len(self._seq)))

    def reflections(self) -> Iterator[RingSeq[T]]:
        """The sequence and its reflection.

        Examples:
          >>> [r.to_str() for r in RingSeq("ABC").reflections()]
          ['ABC', 'ACB']
        """
        if len(self._seq) == 0:
            return iter(())
        return iter((self, self.reflect_at()))

    def reversions(self) -> Iterator[RingSeq[T]]:
        """The sequence and its reversion.

        Examples:
          >>> [r.to_str() for r in RingSeq("ABC").reversions()]
          ['ABC', 'CBA']
        """
        if len(self._seq) == 0:
            return iter(())
        return iter((self, RingSeq(reversed(self._seq))))

    def rotations_and_reflections(self) -> Iterator[RingSeq[T]]:
        """All rotations of the sequence and of its reflection.

        Examples:
          >>> [r.to_str() for r in RingSeq("ABC").rotations_and_reflections()]
          ['ABC', 'BCA', 'CAB', 'ACB', 'CBA', 'BAC']
        """
        if len(self._seq) == 0:
            return iter(())

        def gen() -> Iterator[RingSeq[T]]:
            for reflection in self.reflections():
                yield from reflection.rotations()

        return gen()

    def grouped(self, size: int) -> Iterator[RingSeq[T]]:
        """Groups the ring in fixed-size blocks, wrapping the last block across the seam.

        Examples:
          >>> [g.to_str() for g in RingSeq("ABCDE").grouped(2)]
          ['AB', 'CD', 'EA']
        """
        n = len(self._seq)
        if n == 0:
            return iter(())
        count = -(-n // size)
        return (self._circular_slice(i * size, i * size + size) for i in range(count))

    def zip_with_index(self, from_: IndexO = 0) -> Iterator[tuple[T, Index]]:
        """Iterates over `(element, original-index)` pairs, starting at `from_`.

        Examples:
          >>> list(RingSeq(("a", "b", "c")).zip_with_index(1))
          [('b', 1), ('c', 2), ('a', 0)]
          >>> list(RingSeq(("a", "b", "c")).zip_with_index())
          [('a', 0), ('b', 1), ('c', 2)]
        """
        n = len(self._seq)
        if n == 0:
            return iter(())
        start = self.index_from(from_)
        return ((x, (start + i) % n) for i, x in enumerate(self.start_at(from_)))

    # ----- Predicates -----

    def _is_transformation_of(
        self,
        that: Iterable[T],
        f: Callable[[RingSeq[T]], Iterator[RingSeq[T]]],
    ) -> bool:
        other = that if isinstance(that, RingSeq) else RingSeq(that)
        if len(self._seq) != len(other):
            return False
        return any(r == other for r in f(self))

    def is_rotation_of(self, that: Iterable[T]) -> bool:
        """Whether this ring is a rotation of `that`.

        Examples:
          >>> RingSeq("ABC").is_rotation_of("BCA")
          True
          >>> RingSeq("ABC").is_rotation_of("ABC")
          True
        """
        return self._is_transformation_of(that, lambda r: r.rotations())

    def is_reflection_of(self, that: Iterable[T]) -> bool:
        """Whether this ring is a reflection of `that`.

        Examples:
          >>> RingSeq("ABC").is_reflection_of("ACB")
          True
        """
        return self._is_transformation_of(that, lambda r: r.reflections())

    def is_reversion_of(self, that: Iterable[T]) -> bool:
        """Whether this ring is a reversion of `that`.

        Examples:
          >>> RingSeq("ABC").is_reversion_of("CBA")
          True
        """
        return self._is_transformation_of(that, lambda r: r.reversions())

    def is_rotation_or_reflection_of(self, that: Iterable[T]) -> bool:
        """Whether this ring is a rotation and/or reflection of `that`.

        Examples:
          >>> RingSeq("ABC").is_rotation_or_reflection_of("BAC")
          True
        """
        return self._is_transformation_of(that, lambda r: r.rotations_and_reflections())

    # ----- Alignment / distance -----

    def align_to(self, that: Iterable[T]) -> Index | None:
        """Rotation offset `k` such that `self.start_at(k) == RingSeq(that)`, or `None`.

        Examples:
          >>> RingSeq((0, 1, 2)).align_to((2, 0, 1))
          2
          >>> RingSeq((0, 1, 2)).align_to((0, 1, 2))
          0
          >>> RingSeq((0, 1, 2)).align_to((1, 0, 2)) is None
          True
        """
        other = that if isinstance(that, RingSeq) else RingSeq(that)
        if len(self._seq) != len(other):
            return None
        if len(self._seq) == 0:
            return 0
        for k in range(len(self._seq)):
            if self.start_at(k) == other:
                return k
        return None

    def hamming_distance(self, that: Iterable[T]) -> int:
        """Number of positional mismatches between this ring and `that`.

        Examples:
          >>> RingSeq((1, 0, 1, 1)).hamming_distance((1, 1, 0, 1))
          2
          >>> RingSeq((1, 2, 3)).hamming_distance((1, 2, 3))
          0

        Raises:
          ValueError: if the sizes differ.
        """
        other = tuple(that)
        if len(self._seq) != len(other):
            raise ValueError("sequences must have the same size")
        return sum(1 for a, b in zip(self._seq, other, strict=True) if a != b)

    def min_rotational_hamming_distance(self, that: Iterable[T]) -> int:
        """Minimum Hamming distance over all rotations of this ring.

        Examples:
          >>> RingSeq((1, 2, 3, 4)).min_rotational_hamming_distance((3, 4, 1, 2))
          0
          >>> RingSeq((0, 0, 1, 1, 0)).min_rotational_hamming_distance((1, 1, 0, 0, 1))
          1

        Raises:
          ValueError: if the sizes differ.
        """
        other = tuple(that)
        n = len(self._seq)
        if n != len(other):
            raise ValueError("sequences must have the same size")
        if n == 0:
            return 0
        a = self._seq
        best = n
        for k in range(n):
            count = sum(1 for x, y in zip(a[k:], other) if x != y)
            if k:
                count += sum(1 for x, y in zip(a[:k], other[n - k:]) if x != y)
            if count < best:
                best = count
                if best == 0:
                    break
        return best

    # ----- Symmetry -----

    def rotational_symmetry(self) -> int:
        """Order of rotational symmetry: number of rotations in which the ring looks the same.

        Examples:
          >>> RingSeq("-|--|--|--|-").rotational_symmetry()
          4
          >>> RingSeq("-|+-|+-|+-|+").rotational_symmetry()
          4
          >>> RingSeq([0, 1, 0, 1]).rotational_symmetry()
          2
        """
        n = len(self._seq)
        if n < 2:
            return 1
        smallest_period = next(
            shift for shift in range(1, n + 1) if n % shift == 0 and self.rotate_left(shift) == self
        )
        return n // smallest_period

    def symmetry_indices(self) -> list[Index]:
        """Reflection shifts: `shift` values such that this ring equals its reversal rotated left.

        Each shift identifies one axis of reflectional symmetry.

        Examples:
          >>> RingSeq("-|--|--|--|-").symmetry_indices()
          [0, 3, 6, 9]
          >>> RingSeq("-|+-|+-|+-|+").symmetry_indices()
          []
        """
        n = len(self._seq)
        if n == 0:
            return []
        reversed_ring = RingSeq(reversed(self._seq))
        return [shift for shift in range(n) if self == reversed_ring.rotate_left(shift)]

    def reflectional_symmetry_axes(self) -> list[tuple[AxisLocation, AxisLocation]]:
        """Axes of reflectional symmetry as pairs of `AxisLocation` values.

        Examples:
          >>> RingSeq((1, 1, 2, 3, 2)).reflectional_symmetry_axes()
          [(Vertex(i=3), Edge(i=0, j=1))]
          >>> RingSeq("ABC").reflectional_symmetry_axes()
          []
        """
        n = len(self._seq)

        def opposite(i: Index) -> Index:
            return (i + n // 2) % n

        axes: list[tuple[AxisLocation, AxisLocation]] = []
        for shift in self.symmetry_indices():
            effective_k = (n - 1 - shift) % n
            if n % 2 != 0:
                v = (effective_k * ((n + 1) // 2)) % n
                axes.append((Vertex(v), Edge(opposite(v), n)))
            elif effective_k % 2 == 0:
                v1 = effective_k // 2
                axes.append((Vertex(v1), Vertex(opposite(v1))))
            else:
                e1 = (effective_k - 1) // 2
                axes.append((Edge(e1, n), Edge(opposite(e1), n)))
        return axes

    def symmetry(self) -> int:
        """Order of reflectional (mirror) symmetry.

        Examples:
          >>> RingSeq("-|--|--|--|-").symmetry()
          4
          >>> RingSeq("-|+-|+-|+-|+").symmetry()
          0
        """
        return len(self.symmetry_indices())

    # ----- Canonical forms -----

    def canonical_index(self) -> Index:
        """Starting index of the lex-smallest rotation (Booth's algorithm, O(n)).

        Examples:
          >>> RingSeq((2, 0, 1)).canonical_index()
          1
          >>> RingSeq(()).canonical_index()
          0
        """
        if len(self._seq) <= 1:
            return 0
        return _least_rotation_booth(self._seq)

    def canonical(self) -> RingSeq[T]:
        """Lexicographically smallest rotation (necklace canonical form).

        Examples:
          >>> RingSeq((2, 0, 1)).canonical().to_tuple()
          (0, 1, 2)
          >>> RingSeq("CAB").canonical().to_str()
          'ABC'
        """
        if len(self._seq) == 0:
            return self
        return self.start_at(self.canonical_index())

    def bracelet(self) -> RingSeq[T]:
        """Lexicographically smallest representative under both rotation and reflection.

        Examples:
          >>> RingSeq((2, 0, 1)).bracelet().to_tuple()
          (0, 1, 2)
          >>> RingSeq("CBA").bracelet().to_str()
          'ABC'
        """
        if len(self._seq) == 0:
            return self
        a = self.canonical()
        b = self.reflect_at().canonical()
        return a if a._seq <= b._seq else b
