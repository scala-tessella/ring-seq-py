import unittest

from ring_seq.RingSeq import RingSeq


class RingSeqOps(unittest.TestCase):

    def setUp(self):
        self.ring: RingSeq = RingSeq("ABCDE")
        self.squaroid: RingSeq = RingSeq((2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2))

    def test_indexing(self):
        self.assertEqual(self.ring.index_from(-1), 4)
        self.assertEqual(self.ring.apply_o(-1), "E")

    def test_transforming(self):
        self.assertEqual(self.ring.rotate_right(1), "EABCD")
        self.assertEqual(self.ring.rotate_left(1), "BCDEA")
        self.assertEqual(self.ring.start_at(1), "BCDEA")
        self.assertEqual(self.ring.reflect_at(), "AEDCB")
        self.assertEqual(self.ring.reflect_at(0), "AEDCB")

    def test_slicing(self):
        self.assertEqual(self.ring.slice_o(-1, 6), "EABCDEA")

    def test_iterating(self):
        self.assertEqual(list(self.ring.rotations()), ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"])
        self.assertEqual(list(self.ring.reflections()), ["ABCDE", "AEDCB"])
        self.assertEqual(list(self.ring.reversions()), ["ABCDE", "EDCBA"])
        self.assertEqual(
            list(self.ring.rotations_and_reflections()),
            [
                "ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD",
                "AEDCB", "EDCBA", "DCBAE", "CBAED", "BAEDC"
            ]
        )

    def test_comparing(self):
        self.assertTrue(self.ring.is_rotation_of("CDEAB"))
        self.assertTrue(self.ring.is_reflection_of("AEDCB"))
        self.assertTrue(self.ring.is_reversion_of("EDCBA"))
        self.assertTrue(self.ring.is_rotation_or_reflection_of("CBAED"))

    def test_symmetry(self):
        self.assertEqual(self.squaroid.rotational_symmetry(), 4)
        self.assertEqual(self.squaroid.symmetry_indices(), [1, 4, 7, 10])
        self.assertEqual(self.squaroid.symmetry(), 4)


if __name__ == '__main__':
    unittest.main()
