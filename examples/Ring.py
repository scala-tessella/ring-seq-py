from typing import Any
from ring_seq import IndexO, Seq, apply_o, reflect_at, start_at


class Ring:
    def __init__(self, underlying: Seq, head_index: IndexO = 0, is_reflected: bool = False):
        self.underlying = underlying
        self.head_index = head_index
        self.is_reflected = is_reflected

    def __direction_multiplier(self) -> int:
        if self.is_reflected:
            return 1
        else:
            return -1

    def rotate_r(self, step: int = 1):
        self.head_index += step * self.__direction_multiplier()

    def rotate_l(self, step: int = 1):
        self.rotate_r(-step)

    def reflect(self):
        self.is_reflected = not self.is_reflected

    def current_head(self) -> Any:
        return apply_o(self.underlying, self.head_index)

    def current(self) -> Seq:
        if self.is_reflected:
            return reflect_at(self.underlying, self.head_index)
        else:
            return start_at(self.underlying, self.head_index)
