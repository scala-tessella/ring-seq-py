from ring_seq.methods import *


class RingSeq:
    def __init__(self, underlying: Seq):
        """

        :type underlying: Seq
        """
        self.underlying = underlying

    def index_from(self, i: IndexO) -> Index:
        """

        :type i: IndexO
        """
        return index_from(self.underlying, i)

    def apply_o(self, i: IndexO) -> Any:
        """

        :type i: IndexO
        """
        return apply_o(self.underlying, i)

    def rotate_right(self, step: IndexO) -> Seq:
        """

        :type step: IndexO
        """
        return rotate_right(self.underlying, step)

    def rotate_left(self, step: IndexO) -> Seq:
        """

        :type step: IndexO
        """
        return rotate_left(self.underlying, step)

    def start_at(self, i: IndexO) -> Seq:
        """

        :type i: IndexO
        """
        return start_at(self.underlying, i)

    def reflect_at(self, i: IndexO = 0) -> Seq:
        """

        :type i: IndexO, default = 0
        """
        return reflect_at(self.underlying, i)

    def slice_o(self, frm: IndexO, to: IndexO) -> Seq:
        """

        :type frm: IndexO
        :type to: IndexO
        """
        return slice_o(self.underlying, frm, to)

    def rotations(self) -> Iterator[Seq]:
        return rotations(self.underlying)

    def reflections(self) -> Iterator[Seq]:
        return reflections(self.underlying)

    def reversions(self) -> Iterator[Seq]:
        return reversions(self.underlying)

    def rotations_and_reflections(self) -> Iterator[Seq]:
        return rotations_and_reflections(self.underlying)

    def is_rotation_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return is_rotation_of(self.underlying, that)

    def is_reflection_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return is_reflection_of(self.underlying, that)

    def is_reversion_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return is_reversion_of(self.underlying, that)

    def is_rotation_or_reflection_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return is_rotation_or_reflection_of(self.underlying, that)

    def rotational_symmetry(self) -> int:
        return rotational_symmetry(self.underlying)

    def symmetry_indices(self) -> list[Index]:
        return symmetry_indices(self.underlying)

    def symmetry(self) -> int:
        return symmetry(self.underlying)
