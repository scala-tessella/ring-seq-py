import unittest

from ring_seq import RingSeq


class ComparingOps(unittest.TestCase):
    def test_is_rotation_of(self):
        self.assertTrue(RingSeq("ABCDE").is_rotation_of("CDEAB"))
        self.assertTrue(RingSeq("ABCDE").is_rotation_of("ABCDE"))
        self.assertFalse(RingSeq("ABCDE").is_rotation_of("ABDCE"))
        # cross-type input iterable is OK
        self.assertTrue(RingSeq("ABCDE").is_rotation_of(["C", "D", "E", "A", "B"]))

    def test_is_reflection_of(self):
        self.assertTrue(RingSeq("ABCDE").is_reflection_of("AEDCB"))

    def test_is_reversion_of(self):
        self.assertTrue(RingSeq("ABCDE").is_reversion_of("EDCBA"))

    def test_is_rotation_or_reflection_of(self):
        self.assertTrue(RingSeq("ABCDE").is_rotation_or_reflection_of("CBAED"))

    def test_align_to(self):
        self.assertEqual(RingSeq((0, 1, 2)).align_to((2, 0, 1)), 2)
        self.assertEqual(RingSeq((0, 1, 2)).align_to((0, 1, 2)), 0)
        self.assertIsNone(RingSeq((0, 1, 2)).align_to((1, 0, 2)))
        self.assertIsNone(RingSeq((0, 1, 2)).align_to((0, 1)))
        self.assertEqual(RingSeq(()).align_to(()), 0)
        # align_to agrees with rotations: every rotation has a matching offset
        seq = RingSeq((1, 2, 3, 4, 5))
        for rotation in seq.rotations():
            k = seq.align_to(rotation)
            self.assertIsNotNone(k)
            self.assertEqual(seq.start_at(k), rotation)

    def test_hamming_distance(self):
        self.assertEqual(RingSeq((1, 0, 1, 1)).hamming_distance((1, 1, 0, 1)), 2)
        self.assertEqual(RingSeq((1, 2, 3)).hamming_distance((1, 2, 3)), 0)
        with self.assertRaises(ValueError):
            RingSeq((1, 2)).hamming_distance((1, 2, 3))

    def test_min_rotational_hamming_distance(self):
        self.assertEqual(
            RingSeq((1, 2, 3, 4)).min_rotational_hamming_distance((3, 4, 1, 2)),
            0,
        )
        self.assertEqual(
            RingSeq((0, 0, 1, 1, 0)).min_rotational_hamming_distance((1, 1, 0, 0, 1)),
            1,
        )
        self.assertEqual(RingSeq(()).min_rotational_hamming_distance(()), 0)
        with self.assertRaises(ValueError):
            RingSeq((1, 2)).min_rotational_hamming_distance((1, 2, 3))


if __name__ == "__main__":
    unittest.main()
