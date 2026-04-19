# **RingSeqPy**

A library that extends Python's sequences with circular operations through a single class, `RingSeq`.
Use it when your data is structured as a ring — when the last element is adjacent to the first.

Working for Python `3.10` and above.

### Installation
```
pip install ring-seq-py
```

### Get started

```pycon
>>> from ring_seq import RingSeq

>>> RingSeq('RING').rotate_right(1).to_str()
'GRIN'
>>> RingSeq([0, 1, 2, 3]).start_at(2).to_list()
[2, 3, 0, 1]
>>> RingSeq((1, 3, 5, 7, 9)).reflect_at(3).to_tuple()
(7, 5, 3, 1, 9)
```

A `RingSeq` wraps any iterable. All transformations return a new `RingSeq`; call
`to_list()`, `to_tuple()`, or `to_str()` to unwrap at the boundary. Native Python
protocols work circularly out of the box:

```pycon
>>> r = RingSeq('ABC')
>>> r[-1]        # circular indexing
'C'
>>> r[30001]
'B'
>>> r[-1:5].to_str()   # circular slicing
'CABCAB'
>>> len(r), 'B' in r
(3, True)
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
