# What is a circular sequence

For our purposes, a circular sequence is a sequence composed by a finite number of elements forming a ring.

![circular](circular_plain.svg)

Being circular, the first element of the sequence can be considered as also placed just after the last element.

```python
from ring_seq import RingSeq

RingSeq([0, 1, 2]).apply_o(3) // 0
```

And the last just before the first.

```python
from ring_seq import RingSeq

RingSeq([0, 1, 2]).apply_o(-1) // 2
```

So the "unrolling" of a circular sequence, both forth and backwards, can be assumed as theoretically infinite.

```python
from ring_seq import RingSeq

RingSeq([0, 1, 2]).apply_o(30001) // 1
```
