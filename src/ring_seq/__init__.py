"""Adds circular operations to sequences.

The library exposes a single class, `RingSeq`, that wraps any `Iterable`
and exposes ring operations. Use `to_list()`, `to_tuple()`, or `to_str()`
to unwrap at the boundary.

Typical usage:

    >>> from ring_seq import RingSeq
    >>> RingSeq("RING").rotate_right(1).to_str()
    'GRIN'
    >>> RingSeq([0, 1, 2, 3]).start_at(2).to_list()
    [2, 3, 0, 1]
    >>> RingSeq((1, 3, 5, 7, 9)).reflect_at(3).to_tuple()
    (7, 5, 3, 1, 9)
"""

from ring_seq.ring_seq import AxisLocation, Edge, Index, IndexO, RingSeq, Vertex

__all__ = ["AxisLocation", "Edge", "Index", "IndexO", "RingSeq", "Vertex"]
