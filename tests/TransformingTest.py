import unittest

from ring_seq import RingSeq


class TransformingOps(unittest.TestCase):
    def test_rotate_right(self):
        self.assertEqual(RingSeq("ABCDE").rotate_right(0).to_str(), "ABCDE")
        self.assertEqual(RingSeq("ABCDE").rotate_right(1).to_str(), "EABCD")
        self.assertEqual(RingSeq("ABCDE").rotate_right(6).to_str(), "EABCD")
        self.assertEqual(RingSeq("ABCDE").rotate_right(-4).to_str(), "EABCD")
        self.assertEqual(
            RingSeq(["A", 1, "B", 2]).rotate_right(3).to_list(),
            [1, "B", 2, "A"],
        )
        self.assertEqual(
            RingSeq(("A", 1, "B", 2)).rotate_right(-1).to_tuple(),
            (1, "B", 2, "A"),
        )

    def test_rotate_left(self):
        self.assertEqual(RingSeq("ABCDE").rotate_left(0).to_str(), "ABCDE")
        self.assertEqual(RingSeq("ABCDE").rotate_left(1).to_str(), "BCDEA")
        self.assertEqual(RingSeq("ABCDE").rotate_left(6).to_str(), "BCDEA")
        self.assertEqual(RingSeq("ABCDE").rotate_left(-4).to_str(), "BCDEA")
        self.assertEqual(
            RingSeq(["A", 1, "B", 2]).rotate_left(3).to_list(),
            [2, "A", 1, "B"],
        )
        self.assertEqual(
            RingSeq(("A", 1, "B", 2)).rotate_left(-1).to_tuple(),
            (2, "A", 1, "B"),
        )

    def test_start_at(self):
        self.assertEqual(RingSeq("ABCDE").start_at(0).to_str(), "ABCDE")
        self.assertEqual(RingSeq("ABCDE").start_at(1).to_str(), "BCDEA")
        self.assertEqual(RingSeq("ABCDE").start_at(6).to_str(), "BCDEA")

    def test_reflect_at(self):
        self.assertEqual(RingSeq("ABCDE").reflect_at().to_str(), "AEDCB")
        self.assertEqual(RingSeq("ABCDE").reflect_at(0).to_str(), "AEDCB")
        self.assertEqual(
            RingSeq(["A", 1, "B", 2]).reflect_at(0).to_list(),
            ["A", 2, "B", 1],
        )
        self.assertEqual(
            RingSeq(("A", 1, "B", 2)).reflect_at(0).to_tuple(),
            ("A", 2, "B", 1),
        )


if __name__ == "__main__":
    unittest.main()
