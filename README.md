# **RingSeqPy**

[![PyPI - Version](https://img.shields.io/pypi/v/ring-seq-py?style=plastic&logo=python&logoColor=%234B8BBE&link=https%3A%2F%2Fpypi.org%2Fproject%2Fring-seq-py%2F)](https://pypi.python.org/pypi/ring-seq-py)
[![CI](https://github.com/scala-tessella/ring-seq-py/actions/workflows/python-package.yml/badge.svg)](https://github.com/scala-tessella/ring-seq-py/actions/workflows/python-package.yml)
[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fscala-tessella%2Fring-seq-py%2Fmaster%2Fpyproject.toml&style=plastic&logo=python&logoColor=%23FFD43B)](https://pypi.python.org/pypi/ring-seq-py)

A Pythonic class for sequences considered [**circular**](https://scala-tessella.github.io/ring-seq-py/what-is/) —
where the element after the last wraps back to the first.

`RingSeqPy` is a small, zero-dependency library exposing a single generic
`RingSeq[T]` class that wraps any `Iterable[T]`, stores it internally as an
immutable tuple, and implements the Python `Sequence` protocol circularly.
Instances are hashable, orderable, and interoperable: `RingSeq('ABC')`,
`RingSeq(['A','B','C'])`, and `RingSeq(('A','B','C'))` all compare equal.

## Installation

```
pip install ring-seq-py
```

Working for Python `3.10` and above.

## Quick start

```pycon
>>> from ring_seq import RingSeq

>>> # Indexing wraps around
>>> RingSeq([10, 20, 30])[4]
20

>>> # Slicing wraps around too; transformations return a new RingSeq,
>>> # unwrap with .to_list() / .to_tuple() / .to_str()
>>> RingSeq([0, 1, 2]).rotate_right(1).to_list()
[2, 0, 1]

>>> # Comparison up to rotation
>>> RingSeq([0, 1, 2]).is_rotation_of([2, 0, 1])
True

>>> # Canonical (necklace) form for deduplication
>>> RingSeq([2, 0, 1]).canonical().to_list()
[0, 1, 2]

>>> # Symmetry detection
>>> RingSeq([0, 1, 0, 1]).rotational_symmetry()
2

>>> # Strings work naturally; to_str() rejoins
>>> RingSeq('RING').rotate_right(1).to_str()
'GRIN'
```

## Operations

### Native sequence protocol (circular)

| Method | Description |
|---|---|
| `rs[i]` | Element at circular index (any integer wraps) |
| `rs[i:j]`, `rs[i:j:k]` | Circular slice (can exceed ring length) |
| `len(rs)`, `iter(rs)`, `x in rs` | Standard protocol, no surprises |
| `rs == other`, `hash(rs)`, `min(rings)` | Positional equality; lexicographic ordering |
| `index(value, start=0, stop=None)` | Circular first-occurrence lookup |

### Unwrap

| Method | Description |
|---|---|
| `to_list()` | Return a new `list` |
| `to_tuple()` | Return the internal tuple |
| `to_str(sep='')` | Join elements into a `str` |

### Indexing helper

| Method | Description |
|---|---|
| `index_from(i)` | Normalize a circular index to `[0, len)` |

### Transforming

| Method | Description |
|---|---|
| `rotate_right(step)` | Rotate right by `step` (negative = left) |
| `rotate_left(step)` | Rotate left by `step` (negative = right) |
| `start_at(i)` | Rotate so circular index `i` is first |
| `reflect_at(i=0)` | Reflect so circular index `i` is the axis head |

### Slicing primitives

| Method | Description |
|---|---|
| `take_while(p, from_=0)` | Longest prefix from `from_` satisfying `p` |
| `drop_while(p, from_=0)` | Remainder after that prefix |
| `span(p, from_=0)` | `(take_while, drop_while)` in one call |

### Iterating

| Method | Description |
|---|---|
| `rotations()` | All `n` rotations (lazy) |
| `reflections()` | Original + reflection (lazy) |
| `reversions()` | Original + reversal (lazy) |
| `rotations_and_reflections()` | All `2n` variants (lazy) |
| `grouped(size)` | `ceil(n / size)` fixed-size blocks, last one wraps the seam |
| `zip_with_index(from_=0)` | Elements paired with their circular indices |

### Comparing

| Method | Description |
|---|---|
| `is_rotation_of(that)` | Same elements, possibly rotated? |
| `is_reflection_of(that)` | Same elements, possibly reflected? |
| `is_reversion_of(that)` | Same elements, possibly reversed? |
| `is_rotation_or_reflection_of(that)` | Either of the above? |
| `align_to(that)` | `k` such that `start_at(k) == that`, or `None` |
| `hamming_distance(that)` | Positional mismatches (same size required) |
| `min_rotational_hamming_distance(that)` | Minimum distance over all rotations |

### Necklace

| Method | Description |
|---|---|
| `canonical_index()` | Index of lex-smallest rotation (Booth's *O(n)*) |
| `canonical()` | Lex-smallest rotation (necklace form) |
| `bracelet()` | Lex-smallest under rotation *and* reflection |

### Symmetry

| Method | Description |
|---|---|
| `rotational_symmetry()` | Order of rotational symmetry |
| `symmetry_indices()` | Shifts where the ring equals its reversal rotated left |
| `reflectional_symmetry_axes()` | Full axis geometry (`Vertex` / `Edge` pairs) |
| `symmetry()` | Number of reflectional symmetry axes |

## Naming convention

`RingSeq` subclasses `collections.abc.Sequence`, so native Python protocols
do the work where they map cleanly — `rs[i]` for indexing, `rs[i:j]` for
slicing, `x in rs` for containment. A few methods are deliberately renamed
from the Scala/Rust counterparts to be Pythonic:

| This library | Elsewhere |
|---|---|
| `rs[i]` | `apply_o`  |
| `rs[i:j]`, `rs[i:j:k]` | `slice_o` |
| `index` | `index_of_slice` |
| `grouped` | `circular_chunks` |
| `zip_with_index` | `circular_enumerate` |

`RingSeq.index(value, start=0, stop=None)` overrides `Sequence.index` with
*circular* semantics: without a `stop` it searches one full revolution and
returns an index in `[0, len)`.

## Use cases

- **Bioinformatics** — circular DNA/RNA sequence alignment and comparison
- **Graphics** — polygon vertex manipulation, closed curve operations
- **Procedural generation** — tile rings, symmetry-aware pattern generation
- **Music theory** — pitch-class sets, chord inversions
- **Combinatorics** — necklace/bracelet enumeration, Burnside's lemma
- **Embedded / robotics** — circular sensor arrays, rotary encoder positions

## Other languages

The same library, adapted for the specific idiom, is available also for:
- Scala — [ring-seq](https://github.com/scala-tessella/ring-seq)
- Rust — [ring-seq-rs](https://github.com/scala-tessella/ring-seq-rs)

## License

Licensed under either of

- [Apache License, Version 2.0](LICENSE-APACHE)
- [MIT License](LICENSE-MIT)

at your option.
