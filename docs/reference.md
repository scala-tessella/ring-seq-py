# Reference

This page lists all the features provided by the library.

## The `RingSeq` class

`RingSeq[T]` wraps any `Iterable[T]`, storing it internally as an immutable tuple.
The class is generic, hashable, orderable, and implements the Python `Sequence` protocol —
with all built-in operations (`len`, indexing, slicing, iteration, containment) made circular.

Instances are built with the constructor:

```pycon
>>> from ring_seq import RingSeq
>>> RingSeq('ABC')
RingSeq(('A', 'B', 'C'))
```

Equality is positional and is agnostic to the input iterable kind used at construction:

```pycon
>>> RingSeq('ABC') == RingSeq(['A', 'B', 'C']) == RingSeq(('A', 'B', 'C'))
True
```

Use `to_list()`, `to_tuple()`, or `to_str()` to unwrap at the boundary:

```pycon
>>> RingSeq('ABC').rotate_left(1).to_str()
'BCA'
>>> RingSeq([1, 2, 3]).reflect_at().to_list()
[1, 3, 2]
```

## Methods

Methods fall into the following categories:

### Native sequence protocol (circular)
* [`__getitem__`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.__getitem__) — circular indexing and slicing, e.g. `rs[-1]`, `rs[30001]`, `rs[1:10]`
* `__len__`, `__iter__`, `__contains__` — inherited from `collections.abc.Sequence`
* `__eq__`, `__lt__`, `__le__`, `__hash__` — positional comparison and hashing
* [`index`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.index) — circular element lookup

### Unwrap
* [`to_list`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.to_list)
* [`to_tuple`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.to_tuple)
* [`to_str`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.to_str)

### Indexing helper
* [`index_from`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.index_from)

### Rotation and reflection
* [`rotate_right`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.rotate_right)
* [`rotate_left`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.rotate_left)
* [`start_at`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.start_at)
* [`reflect_at`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.reflect_at)

### Slicing primitives
* [`take_while`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.take_while)
* [`drop_while`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.drop_while)
* [`span`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.span)

### Iterators
* [`rotations`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.rotations)
* [`reversions`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.reversions)
* [`reflections`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.reflections)
* [`rotations_and_reflections`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.rotations_and_reflections)
* [`grouped`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.grouped)
* [`zip_with_index`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.zip_with_index)

### Comparisons
* [`is_reflection_of`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.is_reflection_of)
* [`is_reversion_of`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.is_reversion_of)
* [`is_rotation_of`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.is_rotation_of)
* [`is_rotation_or_reflection_of`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.is_rotation_or_reflection_of)
* [`align_to`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.align_to)
* [`hamming_distance`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.hamming_distance)
* [`min_rotational_hamming_distance`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.min_rotational_hamming_distance)

### Symmetry
* [`rotational_symmetry`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.rotational_symmetry)
* [`symmetry_indices`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.symmetry_indices)
* [`symmetry`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.symmetry)
* [`reflectional_symmetry_axes`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.reflectional_symmetry_axes)

### Canonical forms (necklace / bracelet)
* [`canonical_index`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.canonical_index) — starting index of the lexicographically smallest rotation (Booth's algorithm, O(n))
* [`canonical`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.canonical) — the lex-smallest rotation; useful for hashing/deduplicating equivalent rings
* [`bracelet`](ring_seq_methods.md/#ring_seq.ring_seq.RingSeq.bracelet) — the lex-smallest representative under both rotation and reflection
