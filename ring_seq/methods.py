from typing import Any, Callable, Optional, Iterator, TypeAlias, TypeVar
from numpy import ceil, fmod

# For improved readability, the index of a collection
Index: TypeAlias = int

# For improved readability, the circular index of a collection
IndexO: TypeAlias = int

# There are Sequence types, for example range, that is difficult to consider circular
Seq = TypeVar("Seq", list, str, tuple)


def index_from(ring: Seq, i: IndexO) -> Index:
    length: int = len(ring)
    if length == 0:
        raise (ArithmeticError("An empty collection has no normalized index"))
    n: IndexO = fmod(i, length)
    if n < 0:
        return n + length
    else:
        return n


def apply_o(ring: Seq, i: IndexO) -> Any:
    return ring[index_from(ring, i)]


def rotate_right(ring: Seq, step: IndexO) -> Seq:
    j: Index = len(ring) - index_from(ring, step)
    return ring[j:] + ring[:j]


def rotate_left(ring: Seq, step: IndexO) -> Seq:
    return rotate_right(ring, -step)


def start_at(ring: Seq, i: IndexO) -> Seq:
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
    return __typed_reverse(start_at(ring, i + 1))


def slice_o(ring: Seq, frm: IndexO, to: IndexO) -> Seq:
    length: int = len(ring)
    if length == 0:
        return ring
    elif frm >= to:
        return ring[:0]
    else:
        gap: int = to - frm
        times: int = int(ceil(gap / length) + 1)
        return (start_at(ring, frm) * times)[:gap]


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
            rs.append(rotate_left(r, step))
        return rs

    return __transformations(ring, func)


def reflections(ring: Seq) -> Iterator[Seq]:
    return __transformations(ring, lambda r: (r, reflect_at(r, 0)))


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


def __are_folds_symmetrical(ring: Seq, n: int) -> bool:
    return rotate_right(ring, int(len(ring) / n)) == ring


def rotational_symmetry(ring: Seq) -> int:
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
    return len(symmetry_indices(ring))
