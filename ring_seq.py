from typing import Callable, Iterator, TypeAlias, TypeVar
from numpy import ceil, fmod

# For improved readability, the index of a collection
Index: TypeAlias = int

# For improved readability, the circular index of a collection
IndexO: TypeAlias = int

# There are Sequence types, for example range, that is difficult to consider circular
Seq = TypeVar("Seq", list, str, tuple)


def index_from(i: IndexO, ring: Seq) -> Index:
    length: int = len(ring)
    if length == 0:
        raise (ArithmeticError("An empty collection has no normalized index"))
    n: IndexO = fmod(i, length)
    if n < 0:
        return n + length
    else:
        return n


def apply_o(i: IndexO, ring: Seq) -> Seq:
    return ring[index_from(i, ring)]


def rotate_right(step: IndexO, ring: Seq) -> Seq:
    j: Index = len(ring) - index_from(step, ring)
    return ring[j:] + ring[:j]


def rotate_left(step: IndexO, ring: Seq) -> Seq:
    return rotate_right(-step, ring)


def start_at(i: IndexO, ring: Seq) -> Seq:
    return rotate_left(i, ring)


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


def reflect_at(i: IndexO, ring: Seq) -> Seq:
    return __typed_reverse(start_at(i + 1, ring))


def slice_o(frm: IndexO, to: IndexO, ring: Seq) -> Seq:
    length: int = len(ring)
    if length == 0:
        return ring
    elif frm >= to:
        return ring[:0]
    else:
        gap: int = to - frm
        times: int = int(ceil(gap / length) + 1)
        return (start_at(frm, ring) * times)[:gap]


def __transformations(ring: Seq, f: Callable[[Seq], Seq]) -> Iterator[Seq]:
    """

    :rtype: object
    """
    return iter(f(ring))


def rotations(ring: Seq) -> Iterator[Seq]:
    def func(r: Seq) -> list:
        rs: list[Seq] = []
        step: IndexO
        for step in range(len(r)):
            rs.append(rotate_left(step, r))
        return rs

    return __transformations(ring, func)


def reflections(ring: Seq) -> Iterator[Seq]:
    return __transformations(ring, lambda r: (r, reflect_at(0, r)))


def reversions(ring: Seq) -> Iterator[Seq]:
    return __transformations(ring, lambda r: (r, __typed_reverse(r)))


def rotations_and_reflections(ring: Seq) -> Iterator[Seq]:
    def flat_map(f: Callable[[Seq], Iterator[Seq]], xs: Iterator[Seq]) -> list[Seq]:
        ys: list[Seq] = []
        for x in xs:
            ys.extend(f(x))
        return ys

    return __transformations(ring, lambda r: flat_map(rotations, reflections(r)))


def __is_transformation_of(ring: Seq, that: Seq, f: Callable[[Seq], Iterator[Seq]]) -> bool:
    return len(ring) == len(that) and that in f(ring)


def is_rotation_of(ring: Seq, that: Seq) -> bool:
    return __is_transformation_of(ring, that, lambda r: rotations(r))


def is_reflection_of(ring: Seq, that: Seq) -> bool:
    return __is_transformation_of(ring, that, lambda r: reflections(r))


def is_reversion_of(ring: Seq, that: Seq) -> bool:
    return __is_transformation_of(ring, that, lambda r: reversions(r))


def is_rotation_or_reflection_of(ring: Seq, that: Seq) -> bool:
    return __is_transformation_of(ring, that, lambda r: rotations_and_reflections(r))


def are_folds_symmetrical(ring: Seq, n: int) -> bool:
    return rotate_right(int(len(ring) / n), ring) == ring


def rotational_symmetry(ring: Seq) -> int:
    size = len(ring)
    if size < 2:
        return 1
    else:
        elements = range(int(size / 2), 2, -1)
        filtered = list(filter(lambda x: size % x == 0, elements))
        exact_folds_desc: list[int] = [size] + filtered
        return next((n for n in exact_folds_desc if are_folds_symmetrical(ring, n)), 1)
