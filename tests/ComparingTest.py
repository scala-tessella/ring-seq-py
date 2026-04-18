import unittest

from ring_seq.methods import (
    align_to,
    hamming_distance,
    is_reflection_of,
    is_reversion_of,
    is_rotation_of,
    is_rotation_or_reflection_of,
    min_rotational_hamming_distance,
    rotations,
)


class ComparingOps(unittest.TestCase):

    def test_is_rotation_of(self):
        self.assertTrue(is_rotation_of("ABCDE", "CDEAB"))

    def test_is_reflection_of(self):
        self.assertTrue(is_reflection_of("ABCDE", "AEDCB"))

    def test_is_reversion_of(self):
        self.assertTrue(is_reversion_of("ABCDE", "EDCBA"))

    def test_is_rotation_or_reflection_of(self):
        self.assertTrue(is_rotation_or_reflection_of("ABCDE", "CBAED"))

    def test_align_to(self):
        self.assertEqual(align_to((0, 1, 2), (2, 0, 1)), 2)
        self.assertEqual(align_to((0, 1, 2), (0, 1, 2)), 0)
        self.assertIsNone(align_to((0, 1, 2), (1, 0, 2)))
        self.assertIsNone(align_to((0, 1, 2), (0, 1)))
        self.assertEqual(align_to((), ()), 0)
        # align_to agrees with rotations: every rotation has a matching offset
        seq = (1, 2, 3, 4, 5)
        for rotation in rotations(seq):
            k = align_to(seq, rotation)
            self.assertIsNotNone(k)
            from ring_seq.methods import start_at
            self.assertEqual(start_at(seq, k), rotation)

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance((1, 0, 1, 1), (1, 1, 0, 1)), 2)
        self.assertEqual(hamming_distance((1, 2, 3), (1, 2, 3)), 0)
        with self.assertRaises(ValueError):
            hamming_distance((1, 2), (1, 2, 3))

    def test_min_rotational_hamming_distance(self):
        self.assertEqual(min_rotational_hamming_distance((1, 2, 3, 4), (3, 4, 1, 2)), 0)
        # [0,0,1,1,0] rotated by 2 = [1,1,0,0,0] vs [1,1,0,0,1] → 1 mismatch
        self.assertEqual(min_rotational_hamming_distance((0, 0, 1, 1, 0), (1, 1, 0, 0, 1)), 1)
        self.assertEqual(min_rotational_hamming_distance((), ()), 0)
        with self.assertRaises(ValueError):
            min_rotational_hamming_distance((1, 2), (1, 2, 3))


if __name__ == '__main__':
    unittest.main()
