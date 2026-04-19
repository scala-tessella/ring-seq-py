# Usage examples

This page shows examples of how the library can be used.

## `Ring` class

!!! Tip
    The example `Ring` class demonstrates how a mutable ring view can be built on top of the
    immutable `RingSeq` class — keeping separate rotation and reflection states, then combining
    them to reproduce the current orientation.

::: ring_seq.examples.Ring.Ring
    options:
      show_root_heading: true
      show_source: true
