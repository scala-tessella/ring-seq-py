import unittest

from ring_seq import RingSeq


class NecklaceOps(unittest.TestCase):

    def test_canonical_index_empty_and_single(self):
        self.assertEqual(RingSeq(()).canonical_index(), 0)
        self.assertEqual(RingSeq("").canonical_index(), 0)
        self.assertEqual(RingSeq((5,)).canonical_index(), 0)
        self.assertEqual(RingSeq("A").canonical_index(), 0)

    def test_canonical_index_basic(self):
        self.assertEqual(RingSeq((2, 0, 1)).canonical_index(), 1)
        self.assertEqual(RingSeq("CAB").canonical_index(), 1)
        self.assertEqual(RingSeq((0, 1, 2)).canonical_index(), 0)

    def test_canonical_index_is_starting_position_of_lex_smallest_rotation(self):
        for seq in [
            RingSeq((2, 0, 1)),
            RingSeq((3, 1, 2, 0)),
            RingSeq((1, 2, 1, 2, 1, 2)),
            RingSeq("BANANA"),
            RingSeq("CAB"),
        ]:
            expected = min(seq.rotations())
            # Use tuple comparison via _seq for determinism
            self.assertEqual(
                seq.start_at(seq.canonical_index())._seq,
                expected._seq,
            )

    def test_canonical(self):
        self.assertEqual(RingSeq((2, 0, 1)).canonical().to_tuple(), (0, 1, 2))
        self.assertEqual(RingSeq("CAB").canonical().to_str(), "ABC")
        self.assertEqual(RingSeq(()).canonical().to_tuple(), ())
        self.assertEqual(RingSeq((5,)).canonical().to_tuple(), (5,))

    def test_canonical_rotations_equal_iff_canonical_equal(self):
        a = RingSeq((3, 1, 2, 0))
        b = RingSeq((0, 3, 1, 2))
        c = RingSeq((0, 3, 2, 1))
        self.assertEqual(a.canonical(), b.canonical())
        self.assertNotEqual(a.canonical(), c.canonical())

    def test_bracelet(self):
        self.assertEqual(RingSeq((2, 0, 1)).bracelet().to_tuple(), (0, 1, 2))
        self.assertEqual(RingSeq("CBA").bracelet().to_str(), "ABC")
        self.assertEqual(RingSeq(()).bracelet().to_tuple(), ())
        # bracelet is the minimum over rotations and reflections
        seq = RingSeq((1, 3, 2, 4))
        expected = min(seq.rotations_and_reflections())
        self.assertEqual(seq.bracelet(), expected)


if __name__ == "__main__":
    unittest.main()
