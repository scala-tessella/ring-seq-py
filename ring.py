from typing import TypeAlias, TypeVar
from numpy import fmod

# For improved readability, the index of a collection
Index: TypeAlias = int

# For improved readability, the circular index of a collection
IndexO: TypeAlias = int

# There are Sequence types, for example range, that is difficult to consider circular
Seq = TypeVar("Seq", list, str, tuple)


def index_from(i: IndexO, collection: Seq) -> Index:
    length: int = len(collection)
    if length == 0:
        raise (ArithmeticError("An empty collection has no normalized index"))
    n: IndexO = fmod(i, length)
    if n < 0:
        return n + length
    else:
        return n


def apply_o(i: IndexO, collection: Seq) -> Seq:
    return collection[index_from(i, collection)]


def rotate_right(step: IndexO, collection: Seq) -> Seq:
    j: Index = len(collection) - index_from(step, collection)
    return collection[j:] + collection[:j]


def rotate_left(step: IndexO, collection: Seq) -> Seq:
    return rotate_right(-step, collection)


def start_at(i: IndexO, collection: Seq) -> Seq:
    return rotate_left(i, collection)


def __typed_reverse(collection: Seq) -> Seq:
    rev: reversed = reversed(collection)
    if type(collection) is str:
        return "".join(rev)
    elif type(collection) is list:
        return list(rev)
    elif type(collection) is tuple:
        return tuple(rev)
    else:
        raise (TypeError("Unexpected type, currently str, list and tuple checked"))


def reflect_at(i: IndexO, collection: Seq) -> Seq:
    return __typed_reverse(start_at(i + 1, collection))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(index_from(-1, "ABCDE"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
