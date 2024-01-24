"""Contains all the library methods plus new types.

They add new operations to `list`, `tuple` and `str`
(together represente by type `Seq`)
for when such a sequence needs to be considered **circular**,
its elements forming a ring.

Typical usage example:
  >>> rotate_left('ABC', 1)
  'BCA'
"""
from functools import reduce
from typing import Any, Callable, Optional, Iterator, TypeAlias, TypeVar
from math import ceil, fmod

# For improved readability, the index of a collection
Index: TypeAlias = int

# For improved readability, the circular index of a collection
IndexO: TypeAlias = int

# There are Sequence types, for example range, that is difficult to consider circular
Seq = TypeVar("Seq", list, str, tuple)


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


def rotate_right(ring: Seq, step: IndexO) -> Seq:
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


def rotate_left(ring: Seq, step: IndexO) -> Seq:
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


def __typed_reverse(ring: Seq) -> Seq:
    rev: reversed = reversed(ring)
    if type(ring) is str:
        return "".join(rev)
    elif type(ring) is list:
        return list(rev)
    elif type(ring) is tuple:
        return tuple(rev)
    else:
        raise (TypeError("Unexpected type, currently str, list and tuple checked"))


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


def slice_o(ring: Seq, frm: IndexO, to: IndexO, step: int = 1) -> Seq:
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
      frm: circular index where the slice starts
      to: circular index where the slice ends
      step: number of steps for filtering

    Returns:
      The sliced sequence, with only the first element every each step

    Raises:
      ValueError: An error occurs if slice step is zero.
    """
    if step == 0:
        return ring[frm:to:step]
    length: int = len(ring)
    if length == 0:
        return ring
    gap: int = to - frm
    if gap < 0 or step < 0:
        return ring[:0]
    else:
        times: int = int(ceil(gap / length) + 1)
        all_elements: Seq = (start_at(ring, frm) * times)[:gap]
        if step == 1:
            return all_elements
        else:
            filtered_indices: Iterator[Index] = filter(lambda i: i % step == 0, range(gap))
            filtered_elements: Iterator[Any] = map(lambda i: all_elements[i], filtered_indices)
            return reduce(lambda acc, elem: acc + elem, filtered_elements, ring[:0])


def __transformations(ring: Seq, f: Callable[[Seq], Seq]) -> Iterator[Seq]:
    if len(ring) == 0:
        return iter(ring)
    else:
        return iter(f(ring))


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

    def __func(r: Seq) -> list:
        rs: list[Seq] = []
        step: IndexO
        for step in range(len(r)):
            rs.append(rotate_left(r, step))
        return rs

    return __transformations(ring, __func)


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
    return __transformations(ring, lambda r: (r, reflect_at(r, 0)))


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
    return __transformations(ring, lambda r: (r, __typed_reverse(r)))


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

    def __flat_map(f: Callable[[Seq], Iterator[Seq]], xs: Iterator[Seq]) -> list[Seq]:
        ys: list[Seq] = []
        for x in xs:
            ys.extend(f(x))
        return ys

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
    size = len(ring)
    if size < 2:
        return 1
    else:
        divisors_in_decreasing_size: range = range(int(size / 2), 2, -1)
        exact_divisors: list = list(filter(lambda x: size % x == 0, divisors_in_decreasing_size))
        all_folds_in_decreasing_size: list[int] = [size] + exact_divisors
        return next((folds for folds in all_folds_in_decreasing_size if __are_folds_symmetrical(ring, folds)), 1)


def __greater_half_range(ring: Seq) -> range:
    return range(0, int(ceil(len(ring) / 2)))


def __check_reflection_axis(ring: Seq, gap: int) -> bool:
    check: Callable[[int], bool] = lambda j: apply_o(ring, j + 1) == apply_o(ring, -(j + gap))
    return all(check(folds) for folds in __greater_half_range(ring))


def __has_head_on_axis(ring: Seq) -> bool:
    return __check_reflection_axis(ring, 1)


def __has_axis_between_head_and_next(ring: Seq) -> bool:
    return __check_reflection_axis(ring, 0)


def __has_axis(ring: Seq) -> bool:
    return __has_head_on_axis(ring) or __has_axis_between_head_and_next(ring)


def __find_reflection_symmetry(ring: Seq) -> Optional[Index]:
    return next((j for j in __greater_half_range(ring) if __has_axis(start_at(ring, j))), None)


def symmetry_indices(ring: Seq) -> list[Index]:
    """Finds the indices of each element of this circular sequence close to an axis of reflectional symmetry.

    Examples:
      >>> symmetry_indices('-|--|--|--|-')
      [1, 4, 7, 10]
      >>> symmetry_indices('-|+-|+-|+-|+')
      []

    Args:
      ring: a sequence

    Returns:
      The indices of each element close to an axis of reflectional symmetry,
      that is a line of symmetry that splits the sequence in two identical halves
    """
    length: int = len(ring)
    if length == 0:
        return []
    else:
        folds: int = rotational_symmetry(ring)
        fold_size: int = int(length / folds)
        maybe_symmetry: Optional[Index] = __find_reflection_symmetry(ring[:fold_size])
        if maybe_symmetry is None:
            return []
        else:
            return list(j * fold_size + maybe_symmetry for j in range(folds))


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
