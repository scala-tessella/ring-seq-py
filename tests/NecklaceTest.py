import unittest

from ring_seq.methods import (
    bracelet,
    canonical,
    canonical_index,
    rotations,
    rotations_and_reflections,
    start_at,
)


class NecklaceOps(unittest.TestCase):

    def test_canonical_index_empty_and_single(self):
        self.assertEqual(canonical_index(()), 0)
        self.assertEqual(canonical_index(""), 0)
        self.assertEqual(canonical_index((5,)), 0)
        self.assertEqual(canonical_index("A"), 0)

    def test_canonical_index_basic(self):
        self.assertEqual(canonical_index((2, 0, 1)), 1)
        self.assertEqual(canonical_index("CAB"), 1)
        self.assertEqual(canonical_index((0, 1, 2)), 0)

    def test_canonical_index_is_starting_position_of_lex_smallest_rotation(self):
        # for any sequence, start_at(canonical_index) equals the minimum rotation
        for seq in [
            (2, 0, 1),
            (3, 1, 2, 0),
            (1, 2, 1, 2, 1, 2),
            "BANANA",
            "CAB",
        ]:
            expected = min(rotations(seq))
            self.assertEqual(start_at(seq, canonical_index(seq)), expected)

    def test_canonical(self):
        self.assertEqual(canonical((2, 0, 1)), (0, 1, 2))
        self.assertEqual(canonical("CAB"), "ABC")
        self.assertEqual(canonical(()), ())
        self.assertEqual(canonical((5,)), (5,))

    def test_canonical_rotations_equal_iff_canonical_equal(self):
        a = (3, 1, 2, 0)
        b = (0, 3, 1, 2)
        c = (0, 3, 2, 1)
        self.assertEqual(canonical(a), canonical(b))
        self.assertNotEqual(canonical(a), canonical(c))

    def test_bracelet(self):
        self.assertEqual(bracelet((2, 0, 1)), (0, 1, 2))
        self.assertEqual(bracelet("CBA"), "ABC")
        self.assertEqual(bracelet(()), ())
        # bracelet is the minimum over rotations and reflections
        seq = (1, 3, 2, 4)
        expected = min(rotations_and_reflections(seq))
        self.assertEqual(bracelet(seq), expected)


if __name__ == '__main__':
    unittest.main()
