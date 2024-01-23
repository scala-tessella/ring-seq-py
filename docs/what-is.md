# What is a circular sequence

For our purposes, a circular sequence is a sequence composed by a finite number of elements forming a ring.

![circular](img/circular_plain.svg)

Being circular, the first element of the sequence can be considered as also placed just after the last element.

```pycon
from ring_seq import RingSeq

>>> RingSeq("ABC").apply_o(3)
'A'
```

And the last just before the first.

```pycon
from ring_seq import RingSeq

>>> RingSeq("ABC").apply_o(-1)
'C'
```

So the "unrolling" of a circular sequence, both forth and backwards, can be assumed as theoretically infinite.

```pycon
from ring_seq import RingSeq

>>> RingSeq("ABC").apply_o(30001)
'B'
```
