from typing import Any, Iterator

import ring_seq
from ring_seq import Index, IndexO, Seq


class RingSeq:
    def __init__(self, underlying: Seq):
        self.underlying = underlying

    def index_from(self, i: IndexO) -> Index:
        return ring_seq.index_from(self.underlying, i)

    def apply_o(self, i: IndexO) -> Any:
        return ring_seq.apply_o(self.underlying, i)

    def rotate_right(self, step: IndexO) -> Seq:
        return ring_seq.rotate_right(self.underlying, step)

    def rotate_left(self, step: IndexO) -> Seq:
        return ring_seq.rotate_left(self.underlying, step)

    def start_at(self, i: IndexO) -> Seq:
        return ring_seq.start_at(self.underlying, i)

    def reflect_at(self, i: IndexO = 0) -> Seq:
        return ring_seq.reflect_at(self.underlying, i)

    def slice_o(self, frm: IndexO, to: IndexO) -> Seq:
        return ring_seq.slice_o(self.underlying, frm, to)

    def rotations(self) -> Iterator[Seq]:
        return ring_seq.rotations(self.underlying)

    def reflections(self) -> Iterator[Seq]:
        return ring_seq.reflections(self.underlying)

    def reversions(self) -> Iterator[Seq]:
        return ring_seq.reversions(self.underlying)

    def rotations_and_reflections(self) -> Iterator[Seq]:
        return ring_seq.rotations_and_reflections(self.underlying)

    def is_rotation_of(self, that: Seq) -> bool:
        return ring_seq.is_rotation_of(self.underlying, that)

    def is_reflection_of(self, that: Seq) -> bool:
        return ring_seq.is_reflection_of(self.underlying, that)

    def is_reversion_of(self, that: Seq) -> bool:
        return ring_seq.is_reversion_of(self.underlying, that)

    def is_rotation_or_reflection_of(self, that: Seq) -> bool:
        return ring_seq.is_rotation_or_reflection_of(self.underlying, that)

    def rotational_symmetry(self) -> int:
        return ring_seq.rotational_symmetry(self.underlying)

    def symmetry_indices(self) -> list[Index]:
        return ring_seq.symmetry_indices(self.underlying)

    def symmetry(self) -> int:
        return ring_seq.symmetry(self.underlying)
