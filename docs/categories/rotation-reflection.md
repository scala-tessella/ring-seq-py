# Rotation and reflection

## `rotate_right`

Returns a sequence rotated to the right.

### Example

```scala
Seq(0, 1, 2).rotate_right(1) // Seq(2, 0, 1)
```

##`rotate_left`

Returns a sequence rotated to the left.

### Example

```scala
Seq(0, 1, 2).rotate_left(1) // Seq(1, 2, 0)
```

##`start_at`

Returns a sequence rotated to start at circular index.

@@@ note

Is equivalent to [`rotate_left`](rotation-reflection.html#rotateleft).

@@@

### Example

```scala
Seq(0, 1, 2).start_at(1) // Seq(1, 2, 0)
```

##`reflect_at`

Returns a sequence reversed and rotated to start at circular index.

@@@ note

`reflect_at(-1)` is equivalent to `reverse`.

@@@

### Example

```scala
Seq(0, 1, 2).reflect_at() // Seq(0, 2, 1)
```
