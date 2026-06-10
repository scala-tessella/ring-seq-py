import unittest

from ring_seq import RingSeq


class IndexingOps(unittest.TestCase):
    def test_index_from(self):
        self.assertEqual(RingSeq("ABCDE").index_from(-1), 4)
        self.assertEqual(RingSeq("ABCDE").index_from(5), 0)
        self.assertEqual(RingSeq(["A", 1, "B", 2]).index_from(-1), 3)
        self.assertEqual(RingSeq(("A", 1, "B", 2)).index_from(-1), 3)
        with self.assertRaises(ArithmeticError):
            RingSeq([]).index_from(0)

    def test_getitem_circular(self):
        self.assertEqual(RingSeq("ABCDE")[-1], "E")
        self.assertEqual(RingSeq("ABCDE")[5], "A")
        self.assertEqual(RingSeq("ABC")[30001], "B")
        with self.assertRaises(IndexError):
            RingSeq([])[0]

    def test_get(self):
        self.assertEqual(RingSeq("ABCDE").get(-1), "E")
        self.assertEqual(RingSeq("ABCDE").get(5), "A")
        self.assertIsNone(RingSeq([]).get(0))
        self.assertEqual(RingSeq([]).get(0, "fallback"), "fallback")

    def test_len_and_iter(self):
        self.assertEqual(len(RingSeq("ABC")), 3)
        self.assertEqual(list(iter(RingSeq("ABC"))), ["A", "B", "C"])

    def test_reversed(self):
        self.assertEqual(list(reversed(RingSeq("ABC"))), ["C", "B", "A"])
        self.assertEqual(list(reversed(RingSeq([]))), [])

    def test_contains(self):
        self.assertIn("B", RingSeq("ABC"))
        self.assertNotIn("Z", RingSeq("ABC"))

    def test_equality_cross_type(self):
        # positional equality across input iterable kinds
        self.assertEqual(RingSeq("ABC"), RingSeq(["A", "B", "C"]))
        self.assertEqual(RingSeq((1, 2, 3)), RingSeq([1, 2, 3]))
        self.assertEqual(hash(RingSeq("ABC")), hash(RingSeq(["A", "B", "C"])))

    def test_repr(self):
        self.assertEqual(repr(RingSeq("ABC")), "RingSeq(('A', 'B', 'C'))")


if __name__ == "__main__":
    unittest.main()
