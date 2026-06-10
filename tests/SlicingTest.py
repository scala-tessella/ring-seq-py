import unittest

from ring_seq import RingSeq


class SlicingOps(unittest.TestCase):
    def test_circular_slice(self):
        self.assertEqual(RingSeq("ABCDE")[-1:6].to_str(), "EABCDEA")
        self.assertEqual(RingSeq("ABCDE")[-1:6:2].to_str(), "EBDA")
        self.assertEqual(RingSeq("ABCDE")[1:3].to_str(), "BC")
        self.assertEqual(RingSeq("ABCDE")[3:3].to_str(), "")
        self.assertEqual(RingSeq("ABCDE")[4:3].to_str(), "")
        self.assertEqual(RingSeq("ABCDE")[0:5:2].to_str(), "ACE")
        self.assertEqual(RingSeq("ABCDE")[0:5:3].to_str(), "AD")
        self.assertEqual(
            RingSeq(("A", 1, "B", 2))[-1:6:2].to_tuple(),
            (2, 1, 2, 1),
        )
        with self.assertRaises(ValueError):
            _ = RingSeq("ABCDE")[1:3:0]

    def test_circular_slice_negative_step(self):
        self.assertEqual(RingSeq("ABCDE")[::-1].to_str(), "EDCBA")
        self.assertEqual(RingSeq("ABCDE")[4:1:-1].to_str(), "EDC")
        self.assertEqual(RingSeq("ABCDE")[::-2].to_str(), "ECA")
        # wraps backward without clamping
        self.assertEqual(RingSeq("ABCDE")[0:-6:-1].to_str(), "AEDCBA")
        self.assertEqual(RingSeq("")[::-1].to_str(), "")

    def test_index_of_element(self):
        self.assertEqual(RingSeq(["A", 1, "B", 2]).index("A"), 0)
        self.assertEqual(RingSeq(["A", 1, "B", 2]).index("B"), 2)
        self.assertEqual(RingSeq("ABCDE").index("B"), 1)
        # wraps around the ring
        self.assertEqual(RingSeq("ABCDE").index("A", 1), 0)
        self.assertEqual(RingSeq("ABCDE").index("A", 5), 0)
        # respects the stop bound
        with self.assertRaises(ValueError):
            RingSeq("ABCDE").index("E", 2, 4)
        self.assertEqual(RingSeq("ABCDE").index("E", 2, 5), 4)
        # empty ring
        with self.assertRaises(ValueError):
            RingSeq("").index("A")
        with self.assertRaises(ValueError):
            RingSeq([]).index("A")

    def test_take_while(self):
        self.assertEqual(
            RingSeq((0, 1, 2, 3, 4)).take_while(lambda x: x < 3, 1).to_tuple(),
            (1, 2),
        )
        # wraps around the ring
        self.assertEqual(
            RingSeq((0, 1, 2, 3, 4)).take_while(lambda x: x != 1, 3).to_tuple(),
            (3, 4, 0),
        )
        self.assertEqual(
            RingSeq("ABCDE").take_while(lambda c: c < "D").to_str(),
            "ABC",
        )
        self.assertEqual(RingSeq(()).take_while(lambda x: True).to_tuple(), ())

    def test_drop_while(self):
        self.assertEqual(
            RingSeq((0, 1, 2, 3, 4)).drop_while(lambda x: x < 3, 1).to_tuple(),
            (3, 4, 0),
        )
        self.assertEqual(
            RingSeq("ABCDE").drop_while(lambda c: c < "D").to_str(),
            "DE",
        )
        self.assertEqual(RingSeq(()).drop_while(lambda x: True).to_tuple(), ())

    def test_span(self):
        take, drop = RingSeq((0, 1, 2, 3, 4)).span(lambda x: x < 3, 1)
        self.assertEqual(take.to_tuple(), (1, 2))
        self.assertEqual(drop.to_tuple(), (3, 4, 0))
        # agrees with take_while and drop_while
        prefix, suffix = RingSeq((1, 2, 3, 4, 5)).span(lambda x: x < 4, 2)
        self.assertEqual(prefix, RingSeq((1, 2, 3, 4, 5)).take_while(lambda x: x < 4, 2))
        self.assertEqual(suffix, RingSeq((1, 2, 3, 4, 5)).drop_while(lambda x: x < 4, 2))


if __name__ == "__main__":
    unittest.main()
