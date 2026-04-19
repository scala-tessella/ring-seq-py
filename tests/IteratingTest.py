import unittest

from ring_seq import RingSeq


def _strs(ring_iter):
    return [r.to_str() for r in ring_iter]


def _tuples(ring_iter):
    return [r.to_tuple() for r in ring_iter]


class IteratingOps(unittest.TestCase):
    def test_rotations(self):
        self.assertEqual(list(RingSeq([]).rotations()), [])
        self.assertEqual(list(RingSeq("").rotations()), [])
        self.assertEqual(list(RingSeq(()).rotations()), [])
        self.assertEqual(
            _strs(RingSeq("ABCDE").rotations()),
            ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"],
        )

    def test_reflections(self):
        self.assertEqual(list(RingSeq([]).reflections()), [])
        self.assertEqual(list(RingSeq("").reflections()), [])
        self.assertEqual(list(RingSeq(()).reflections()), [])
        self.assertEqual(
            _strs(RingSeq("ABCDE").reflections()),
            ["ABCDE", "AEDCB"],
        )

    def test_reversions(self):
        self.assertEqual(list(RingSeq([]).reversions()), [])
        self.assertEqual(
            _strs(RingSeq("ABCDE").reversions()),
            ["ABCDE", "EDCBA"],
        )
        self.assertEqual(
            _tuples(RingSeq(("A", 1, "B", 2)).reversions()),
            [("A", 1, "B", 2), (2, "B", 1, "A")],
        )

    def test_rotations_and_reflections(self):
        self.assertEqual(list(RingSeq([]).rotations_and_reflections()), [])
        self.assertEqual(
            _strs(RingSeq("ABCDE").rotations_and_reflections()),
            [
                "ABCDE",
                "BCDEA",
                "CDEAB",
                "DEABC",
                "EABCD",
                "AEDCB",
                "EDCBA",
                "DCBAE",
                "CBAED",
                "BAEDC",
            ],
        )
        self.assertEqual(
            _tuples(RingSeq(("A", 1, "B", 2)).rotations_and_reflections()),
            [
                ("A", 1, "B", 2),
                (1, "B", 2, "A"),
                ("B", 2, "A", 1),
                (2, "A", 1, "B"),
                ("A", 2, "B", 1),
                (2, "B", 1, "A"),
                ("B", 1, "A", 2),
                (1, "A", 2, "B"),
            ],
        )

    def test_grouped(self):
        self.assertEqual(
            _strs(RingSeq("ABCDE").grouped(2)),
            ["AB", "CD", "EA", "BC", "DE"],
        )
        self.assertEqual(list(RingSeq("").grouped(2)), [])
        self.assertEqual(list(RingSeq(()).grouped(3)), [])
        self.assertEqual(
            _tuples(RingSeq((0, 1, 2, 3, 4)).grouped(3)),
            [(0, 1, 2), (3, 4, 0), (1, 2, 3), (4, 0, 1), (2, 3, 4)],
        )

    def test_zip_with_index(self):
        self.assertEqual(
            list(RingSeq(("a", "b", "c")).zip_with_index(1)),
            [("b", 1), ("c", 2), ("a", 0)],
        )
        self.assertEqual(
            list(RingSeq(("a", "b", "c")).zip_with_index()),
            [("a", 0), ("b", 1), ("c", 2)],
        )
        self.assertEqual(list(RingSeq(()).zip_with_index()), [])


if __name__ == "__main__":
    unittest.main()
