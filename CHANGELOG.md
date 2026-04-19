# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] — 2026-04-19

**Hard break** — v2 is a ground-up redesign around a single, idiomatic `RingSeq` class.
Code written against 1.x will not work unchanged; see **Migration** below.

### Added
- `RingSeq[T]` class, generic over the element type, wrapping any `Iterable[T]` and
  implementing the Python `Sequence` protocol (`len`, `iter`, `in`, indexing, slicing)
  with circular semantics. Instances are immutable, hashable, and orderable.
- Native circular indexing and slicing via `__getitem__`: `rs[-1]`, `rs[30001]`,
  `rs[1:10]`, `rs[0:5:2]` all work without calling `apply_o` / `slice_o`.
- Explicit unwrap methods: `to_list()`, `to_tuple()`, `to_str(sep="")`.
- Cross-type equality and hashing: `RingSeq('ABC') == RingSeq(['A','B','C']) ==
  RingSeq(('A','B','C'))` — all equal, all share the same hash.
- Ordering (`<`, `<=`, `min()`, sorting) based on lexicographic tuple order.
- New ring operations ported from the Scala library:
  - `take_while`, `drop_while`, `span`
  - `grouped`, `zip_with_index`
  - `align_to`, `hamming_distance`, `min_rotational_hamming_distance`
  - `canonical_index`, `canonical`, `bracelet` (Booth's O(n) algorithm)
  - `reflectional_symmetry_axes` with `AxisLocation` / `Vertex` / `Edge` value types
- Dual-licensed under Apache-2.0 OR MIT.

### Changed
- **Single-class API.** The `RingSeq` class is now the only public entry point;
  the `ring_seq.methods` module and its module-level functions have been removed.
- **No `_o` suffix noise.** Because `RingSeq` is already circular, `slice_o`,
  `index_o`, `take_while_o`, `drop_while_o`, `span_o`, `grouped_o`,
  `zip_with_index_o`, `segment_length_o`, `apply_o` are gone or renamed without
  the suffix.
- **Type preservation is explicit, not implicit.** v1 returned `list`/`str`/`tuple`
  matching the input type via an internal `__typed_assemble`. v2 always returns
  `RingSeq[T]`; the caller unwraps with `to_list()` / `to_str()` / `to_tuple()` at
  the boundary.
- `str` is no longer privileged: `RingSeq("ABC")` stores `('A', 'B', 'C')` like any
  other iterable. Call `.to_str()` to rejoin.
- `Edge` enforces its invariant: `Edge(i, n)` takes the ring size `n` and derives
  `j = (i + 1) % n`. Pattern matching `case Edge(i, j):` still works.
- `symmetry_indices` returns reflection shifts (matching the Scala library's
  semantics), not positional "element-close-to-axis" indices.
- `examples.Ring` rewritten on top of the new class; still preserves the input
  concrete type (`list` / `tuple` / `str`) when exposing `.current()`.

### Removed
- `ring_seq.methods` module — every function is gone. Everything lives on `RingSeq`.
- `ring_seq.RingSeq` module — merged into `ring_seq.ring_seq`; import paths are
  `from ring_seq import RingSeq, Vertex, Edge` (unchanged for users who were using
  the package-level re-export).
- `TypeVar("Seq", list, str, tuple)` — superseded by `Generic[T]` / `Sequence[T]`.
- `apply_o`, `slice_o`, `index_o` (as free functions) — replaced by native
  `rs[i]`, `rs[i:j]`, `rs.index(x)`.

### Migration

| v1 | v2 |
|---|---|
| `from ring_seq.methods import rotate_left` | `from ring_seq import RingSeq` |
| `rotate_left("RING", 1)` → `'INGR'` | `RingSeq("RING").rotate_left(1).to_str()` |
| `apply_o([0,1,2,3], -1)` → `3` | `RingSeq([0,1,2,3])[-1]` |
| `slice_o("ABC", -1, 5)` → `'CABCAB'` | `RingSeq("ABC")[-1:5].to_str()` |
| `index_o("ABC", "B", 2, 7)` → `1` | `RingSeq("ABC").index("B", 2, 7)` |
| `take_while_o(r, p, 1)` | `RingSeq(r).take_while(p, 1)` |
| `Edge(i, (i+1) % n)` | `Edge(i, n)` |
| `RingSeq('-\|--\|--\|--\|-').symmetry_indices()` → `[1, 4, 7, 10]` | `RingSeq('-\|--\|--\|--\|-').symmetry_indices()` → `[0, 3, 6, 9]` (shift-based) |

## [1.0] — earlier

Initial release: Python port of the Scala `ring-seq` library, exposing module-level
functions over `list` / `tuple` / `str` plus a thin `RingSeq` wrapper for dot
notation. See the git history for the feature-by-feature evolution.
