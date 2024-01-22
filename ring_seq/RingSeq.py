from typing import Any, Iterator

import ring_seq.methods
from ring_seq.methods import Index, IndexO, Seq


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
        return ring_seq.methods.index_from(self.underlying, i)

    def apply_o(self, i: IndexO) -> Any:
        """

        :type i: IndexO
        """
        return ring_seq.methods.apply_o(self.underlying, i)

    def rotate_right(self, step: IndexO) -> Seq:
        """

        :type step: IndexO
        """
        return ring_seq.methods.rotate_right(self.underlying, step)

    def rotate_left(self, step: IndexO) -> Seq:
        """

        :type step: IndexO
        """
        return ring_seq.methods.rotate_left(self.underlying, step)

    def start_at(self, i: IndexO) -> Seq:
        """

        :type i: IndexO
        """
        return ring_seq.methods.start_at(self.underlying, i)

    def reflect_at(self, i: IndexO = 0) -> Seq:
        """

        :type i: IndexO, default = 0
        """
        return ring_seq.methods.reflect_at(self.underlying, i)

    def slice_o(self, frm: IndexO, to: IndexO) -> Seq:
        """

        :type frm: IndexO
        :type to: IndexO
        """
        return ring_seq.methods.slice_o(self.underlying, frm, to)

    def rotations(self) -> Iterator[Seq]:
        return ring_seq.methods.rotations(self.underlying)

    def reflections(self) -> Iterator[Seq]:
        return ring_seq.methods.reflections(self.underlying)

    def reversions(self) -> Iterator[Seq]:
        return ring_seq.methods.reversions(self.underlying)

    def rotations_and_reflections(self) -> Iterator[Seq]:
        return ring_seq.methods.rotations_and_reflections(self.underlying)

    def is_rotation_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return ring_seq.methods.is_rotation_of(self.underlying, that)

    def is_reflection_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return ring_seq.methods.is_reflection_of(self.underlying, that)

    def is_reversion_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return ring_seq.methods.is_reversion_of(self.underlying, that)

    def is_rotation_or_reflection_of(self, that: Seq) -> bool:
        """

        :type that: Seq
        """
        return ring_seq.methods.is_rotation_or_reflection_of(self.underlying, that)

    def rotational_symmetry(self) -> int:
        return ring_seq.methods.rotational_symmetry(self.underlying)

    def symmetry_indices(self) -> list[Index]:
        return ring_seq.methods.symmetry_indices(self.underlying)

    def symmetry(self) -> int:
        return ring_seq.methods.symmetry(self.underlying)
