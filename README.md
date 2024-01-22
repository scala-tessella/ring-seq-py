# **RingSeqPy**

A library that adds new operations to Python `list`, `tuple` and `str`
for when such a sequence needs to be considered [**circular**](https://scala-tessella.github.io/ring-seq/what-is.html),
its elements forming a ring.

Available for Python `3.12.1`.

## Setup

```python
from RingSeq import RingSeq

RingSeq("RING").rotate_right(1) # "GRIN"
RingSeq([0, 1, 2, 3]).start_at(2) # [2, 3, 0, 1]
RingSeq((1, 3, 5, 7, 9)).reflect_at(3) # (7, 5, 3, 1, 9)
```

or alternatively, without `class RingSeq` wrapper:

```python
from ring_seq import rotate_right, start_at, reflect_at

rotate_right("RING", 1) # "GRIN"
start_at([0, 1, 2, 3], 2) # [2, 3, 0, 1]
reflect_at((1, 3, 5, 7, 9), 3) # (7, 5, 3, 1, 9)
```

## Testing

Testing made with [`unittest`](https://docs.python.org/3/library/unittest.html)

## Type hints

Supported with [`typing`](https://docs.python.org/3/library/typing.html)