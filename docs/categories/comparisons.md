# Comparisons

## `is_reflection`

Tests if a sequence is a reflection of another one.

@@@ note

A sequence is always a reflection of itself.

@@@

### Example

```scala
Seq(0, 1, 2).is_reflectionOf(Seq(0, 2, 1)) // true
```

## `is_reversion`

Tests if a sequence is a reversion of another one.

@@@ note

A sequence is always a reversion of itself.

@@@

### Example

```scala
Seq(0, 1, 2).is_reversionOf(Seq(2, 1, 0)) // true
```

## `is_rotation`

Tests if a sequence is a rotation of another one.

@@@ note

A sequence is always a rotation of itself.

@@@

### Example

```scala
Seq(0, 1, 2).is_rotationOf(Seq(1, 2, 0)) // true
```

## `is_rotation_or_reflection`

Tests if a sequence is a rotation or a reflection of another one.

@@@ note

A sequence is always a rotation and a reflection of itself.

@@@

### Example

```scala
Seq(0, 1, 2).is_rotation_or_reflection(Seq(2, 0, 1)) // true
```
