from typing import TypeAlias, TypeVar
from numpy import ceil, fmod
from functional import fold_left

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(index_from(-1, "ABCDE"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
