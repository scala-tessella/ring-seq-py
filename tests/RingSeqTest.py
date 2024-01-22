import unittest

from ring_seq.RingSeq import RingSeq
from ring_seq.methods import Index

class RingSeqOps(unittest.TestCase):

    def setUp(self):
        self.ring: RingSeq = RingSeq("ABCDE")
        self.squaroid: RingSeq = RingSeq((2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2))

    def test_indexing(self):
        # circular index -1 of "ABCDE" is equal to index 4
        result: Index = self.ring.index_from(-1)
        self.assertEqual(result, 4)

        # element at index -1 of "ABCDE" is element "E"
        result: str = self.ring.apply_o(-1)
        self.assertEqual(result, 'E')

    def test_transforming(self):
        # "ABCDE" rotated one step to the right is "EABCD"
        result: str = self.ring.rotate_right(1)
        self.assertEqual(result, "EABCD")

        # "ABCDE" rotated one step to the left is "BCDEA"
        result: str = self.ring.rotate_left(1)
        self.assertEqual(result, "BCDEA")

        # "ABCDE" rotated to start at circular index 1 is "BCDEA"
        result: str = self.ring.start_at(1)
        self.assertEqual(result, "BCDEA")

        # "ABCDE" reflected with the same start is "AEDCB"
        result: str = self.ring.reflect_at()
        self.assertEqual(result, "AEDCB")

        # "ABCDE" rotated to start at circular index 1 and reflected is "BAEDC"
        result: str = self.ring.reflect_at(1)
        self.assertEqual(result, "BAEDC")

    def test_slicing(self):
        # "ABCDE" sliced from circular index -1 to circular index 6 is "EABCDEA"
        result: str = self.ring.slice_o(-1, 6)
        self.assertEqual(result, "EABCDEA")

    def test_iterating(self):
        # All 5 "ABCDE" rotations
        result: list[str] = list(self.ring.rotations())
        self.assertEqual(result, ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"])

        # The two "ABCDE" reflections
        result: list[str] = list(self.ring.reflections())
        self.assertEqual(result, ["ABCDE", "AEDCB"])

        # The two "ABCDE" reversions
        result: list[str] = list(self.ring.reversions())
        self.assertEqual(result, ["ABCDE", "EDCBA"])

        # All 10 "ABCDE" rotations and reflections
        result: list[str] = list(self.ring.rotations_and_reflections())
        self.assertEqual(
            result,
            ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD", "AEDCB", "EDCBA", "DCBAE", "CBAED", "BAEDC"]
        )

    def test_comparing(self):
        # "ABCDE" is a rotation of "CDEAB"
        result: bool = self.ring.is_rotation_of("CDEAB")
        self.assertTrue(result)

        # "ABCDE" is a reflection of "AEDCB"
        result: bool = self.ring.is_reflection_of("AEDCB")
        self.assertTrue(result)

        # "ABCDE" is a reflection of "EDCBA"
        result: bool = self.ring.is_reversion_of("EDCBA")
        self.assertTrue(result)

        # "ABCDE" is a rotation and reflection of "CBAED"
        result: bool = self.ring.is_rotation_or_reflection_of("CBAED")
        self.assertTrue(result)

    def test_symmetry(self):
        # (2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2) has 4 rotational symmetries
        result: int = self.squaroid.rotational_symmetry()
        self.assertEqual(result, 4)

        # (2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2) has axis of symmetry at indices 1, 4, 7 and 10
        result: list[Index] = self.squaroid.symmetry_indices()
        self.assertEqual(result, [1, 4, 7, 10])

        # (2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2) has 4 reflectional symmetries
        result: int = self.squaroid.symmetry()
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
