from ring_seq.methods import *


class RingSeq:
    def __init__(self, underlying: Seq):
        """

        :param underlying: sequence considered circular
        :type underlying: Seq
        """
        self.underlying = underlying

    def index_from(self, i: IndexO) -> Index:
        """
        Normalize a given index of a circular Seq

        :param i: circular index
        :type i: Index
        :return: standard index
        :rtype: Any
        """
        return index_from(self.underlying, i)

    def apply_o(self, i: IndexO) -> Any:
        """
        Gets the element at some circular index.

        :param i: circular index
        :type i: IndexO
        :return: element at circular index
        :rtype: Any
        """
        return apply_o(self.underlying, i)

    def rotate_right(self, step: IndexO) -> Seq:
        """
        Rotate the sequence to the right by some steps.

        :param step: number of rotation steps to the right
        :type step: IndexO
        :return: rotated sequence
        :rtype: Seq
        """
        return rotate_right(self.underlying, step)

    def rotate_left(self, step: IndexO) -> Seq:
        """
        Rotate the sequence to the left by some steps.

        :param step: number of rotation steps to the left
        :type step: IndexO
        :return: rotated sequence
        :rtype: Seq
        """
        return rotate_left(self.underlying, step)

    def start_at(self, i: IndexO) -> Seq:
        """
        Rotates the sequence to start at some circular index.

        :param i: circular index where the sequence starts
        :type i: IndexO
        :return: rotated sequence
        :rtype: Seq
        """
        return start_at(self.underlying, i)

    def reflect_at(self, i: IndexO = 0) -> Seq:
        """
        Reflects the sequence to start at some circular index.

        :param i: circular index where the reflected sequence starts
        :type i: IndexO, default = 0
        :return: reflected sequence
        :rtype: Seq
        """
        return reflect_at(self.underlying, i)

    def slice_o(self, frm: IndexO, to: IndexO) -> Seq:
        """
        Selects an interval of elements.

        :param frm: circular index where the slice starts
        :type frm: IndexO
        :param to: circular index where the slice ends
        :type to: IndexO
        :return: sliced sequence
        :rtype: Seq
        """
        return slice_o(self.underlying, frm, to)

    def rotations(self) -> Iterator[Seq]:
        """
        Computes all the rotations of this circular sequence

        :return: sequence and its rotations, 1 step at a time to the right
        :rtype: Iterator[Seq]
        """
        return rotations(self.underlying)

    def reflections(self) -> Iterator[Seq]:
        """
        Computes all the reflections of this circular sequence

        :return: sequence and its reflection
        :rtype: Iterator[Seq]
        """
        return reflections(self.underlying)

    def reversions(self) -> Iterator[Seq]:
        """
        Computes all the reversions of this circular sequence

        :return: sequence and its reversion
        :rtype: Iterator[Seq]
        """
        return reversions(self.underlying)

    def rotations_and_reflections(self) -> Iterator[Seq]:
        """
        Computes all the rotations and reflections of this circular sequence

        :return: sequence and its rotations, and their reflections
        :rtype: Iterator[Seq]
        """
        return rotations_and_reflections(self.underlying)

    def is_rotation_of(self, that: Seq) -> bool:
        """
        Tests whether this circular sequence is a rotation of a given sequence.

        :param that: sequence to be compared
        :type that: Seq
        :return: true if equal to any rotation of that
        :rtype: bool
        """
        return is_rotation_of(self.underlying, that)

    def is_reflection_of(self, that: Seq) -> bool:
        """
        Tests whether this circular sequence is a reflection of a given sequence.

        :param that: sequence to be compared
        :type that: Seq
        :return: true if equal to any reflection of that
        :rtype: bool
        """
        return is_reflection_of(self.underlying, that)

    def is_reversion_of(self, that: Seq) -> bool:
        """
        Tests whether this circular sequence is a reversion of a given sequence.

        :param that: sequence to be compared
        :type that: Seq
        :return: true if equal to any reversion of that
        :rtype: bool
        """
        return is_reversion_of(self.underlying, that)

    def is_rotation_or_reflection_of(self, that: Seq) -> bool:
        """
        Tests whether this circular sequence is a rotation and/or reflection of a given sequence.

        :param that: sequence to be compared
        :type that: Seq
        :return: true if equal to any combination of rotation and reflection of that
        :rtype: bool
        """
        return is_rotation_or_reflection_of(self.underlying, that)

    def rotational_symmetry(self) -> int:
        """
        Computes the order of rotational symmetry possessed by this circular sequence.

        :return: rotational symmetry order
        :rtype: int
        """
        return rotational_symmetry(self.underlying)

    def symmetry_indices(self) -> list[Index]:
        """
        Finds the indices of each element of this circular sequence close to an axis of reflectional symmetry.

        :return: indices of the elements by which the reflectional symmetry axis are near
        :rtype: list[Index]
        """
        return symmetry_indices(self.underlying)

    def symmetry(self) -> int:
        """
        Computes the order of reflectional (mirror) symmetry possessed by this circular sequence.

        :return: reflectional symmetry order
        :rtype: int
        """
        return symmetry(self.underlying)
