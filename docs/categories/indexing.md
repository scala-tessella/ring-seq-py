# Indexing

## `apply_o`

The circular equivalent of `apply`.

@@@ note

Given the [definition of circular sequence](../what-is), it returns an element for any possible integer.

@@@

### Example

```scala
Seq(0, 1, 2).apply_o(3) // 0
```

### Compared to standard

In the same example the standard version behaves differently,
does not return an element, it throws.

```scala
Seq(0, 1, 2).apply(3) // IndexOutOfBoundsException
```

### Not a total function

It does not return a value for an empty sequence.

```scala
Seq.empty.apply_o(0) // ArithmeticException
```

## `index_from`

Converts a circular index into a standard index.

### Example

```scala
Seq(0, 1, 2).index_from(30001) // 1
```
