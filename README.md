# **RingSeqPy**

A library that adds new operations to Python `list`, `tuple` and `str`
for when such a sequence needs to be considered [**circular**](https://scala-tessella.github.io/ring-seq/what-is.html),
its elements forming a ring.

Working for Python `3.10` and above.

### Installation
```
pip install ring-seq-py
```

### Get started

```python
from ring_seq import RingSeq

RingSeq("RING").rotate_right(1)  # "GRIN"
RingSeq([0, 1, 2, 3]).start_at(2)  # [2, 3, 0, 1]
RingSeq((1, 3, 5, 7, 9)).reflect_at(3)  # (7, 5, 3, 1, 9)
```

or alternatively, without the `class RingSeq` wrapper:

```python
from ring_seq.methods import rotate_right, start_at, reflect_at

rotate_right("RING", 1)  # "GRIN"
start_at([0, 1, 2, 3], 2)  # [2, 3, 0, 1]
reflect_at((1, 3, 5, 7, 9), 3)  # (7, 5, 3, 1, 9)
```

## Need
Whenever data are structured in a circular sequence,
chances are you don't want to locally reinvent the wheel (pun intended).

## Solution
**RingSeqPy** is a small, purely functional, self-contained library,
where most of the circular use cases are already solved
and building blocks provided for the others.

## Other languages
The same library is available also for the Scala language, check [RingSeq (Scala version)](https://scala-tessella.github.io/ring-seq/).
