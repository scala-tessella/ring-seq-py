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
* [`index_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.index_o)
* [`take_while_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.take_while_o)
* [`drop_while_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.drop_while_o)
* [`span_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.span_o)

### Iterators
* [`rotations`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotations)
* [`reversions`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.reversions)
* [`reflections`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.reflections)
* [`rotations_and_reflections`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotations_and_reflections)
* [`grouped_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.grouped_o)
* [`zip_with_index_o`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.zip_with_index_o)

### Comparisons
* [`is_reflection`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_reflection)
* [`is_reversion`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_reversion)
* [`is_rotation`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_rotation)
* [`is_rotation_or_reflection`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.is_rotation_or_reflection)
* [`align_to`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.align_to)
* [`hamming_distance`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.hamming_distance)
* [`min_rotational_hamming_distance`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.min_rotational_hamming_distance)

### Symmetry
* [`rotational_symmetry`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.rotational_symmetry)
* [`symmetry_indices`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.symmetry_indices)
* [`symmetry`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.symmetry)
* [`reflectional_symmetry_axes`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.reflectional_symmetry_axes)

### Canonical forms (necklace / bracelet)
* [`canonical_index`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.canonical_index) — starting index of the lexicographically smallest rotation (Booth's algorithm, O(n))
* [`canonical`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.canonical) — the lex-smallest rotation; useful for hashing/deduplicating equivalent rings
* [`bracelet`](ring_seq_methods.md/#ring_seq.RingSeq.RingSeq.bracelet) — the lex-smallest representative under both rotation and reflection
