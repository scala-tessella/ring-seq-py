# Reference

This page shows all the features provided by the library.

## Methods

For dealing with a circular sequence, **RingSeqPy** adds:

1. A type `Seq` representing a sequence of type `list`, `tuple` or `str`.
2. new operations on `Seq`.
3. alternative versions of some operations already existing for `Seq`.

!!! Tip
    Methods in case _3. alternative versions_ have a suffix `_o` in their name, for example `slice_o`.    

!!! Info
    By design choice the same methods are available both in the original form `method(Seq, ...)`
    and in the form `RingSeq(Seq).method(...)` via the wrapper class `RingSeq`,
    in order to allow use of [Dot notation](https://en.wikipedia.org/wiki/Property_(programming)#Dot_notation).

Methods fall into the following categories:

### Indexing
* [`apply_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.apply_o)
* [`index_from`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.index_from)

### Rotation and reflection
* [`rotate_right`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotate_right)
* [`rotate_left`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotate_left)
* [`start_at`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.start_at)
* [`reflect_at`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.reflect_at)

### Slicing
* [`slice_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.slice_o)

### Iterators
* [`rotations`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotations)
* [`reversions`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.reversions)
* [`reflections`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.reflections)
* [`rotations_and_reflections`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotations_and_reflections)

### Comparisons
* [`is_reflection`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_reflection)
* [`is_reversion`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_reversion)
* [`is_rotation`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_rotation)
* [`is_rotation_or_reflection`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_rotation_or_reflection)

### Symmetry
* [`rotational_symmetry`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotational_symmetry)
* [`symmetry_indices`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.symmetry_indices)
* [`symmetry`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.symmetry)
