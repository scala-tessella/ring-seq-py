# Slicing

## `slice_o`

The circular equivalent of `slice`.

@@@ note

Given the [definition of circular sequence](../what-is), a slice can contain more elements than the sequence itself.

@@@

### Example

```scala
Seq(0, 1, 2).slice_o(-1, 4) // Seq(2, 0, 1, 2, 0)
```

### Compared to standard

In the same example the standard version behaves differently,
it is equivalent to `slice(0, 2)`, does not return the "unrolled" slice.

```scala
Seq(0, 1, 2).slice(-1, 4) // Seq(0, 1, 2)
```
