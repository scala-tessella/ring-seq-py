import unittest

from ring_seq.methods import drop_while_o, index_o, slice_o, span_o, take_while_o


class SlicingOps(unittest.TestCase):

    def test_slice_o(self):
        self.assertEqual(slice_o("ABCDE", -1, 6), "EABCDEA")
        self.assertEqual(slice_o("ABCDE", -1, 6, 2), "EBDA")
        self.assertEqual("ABCDE"[1:3], "BC")
        self.assertEqual(slice_o("ABCDE", 1, 3), "BC")
        self.assertEqual(slice_o("ABCDE", 3, 3), "")
        self.assertEqual("ABCDE"[4:3], "")
        self.assertEqual(slice_o("ABCDE", 4, 3), "")
        with self.assertRaises(ValueError):
            var = "ABCDE"[1:3:0]
        with self.assertRaises(ValueError):
            var = slice_o("ABCDE", 1, 3, 0)
        self.assertEqual("ABCDE"[0:5:2], "ACE")
        self.assertEqual(slice_o("ABCDE", 0, 5, 2), "ACE")
        self.assertEqual("ABCDE"[0:5:3], "AD")
        self.assertEqual(slice_o("ABCDE", 0, 5, 3), "AD")
        self.assertEqual("ABCDE"[0:5:2], "ACE")
        self.assertEqual(slice_o(("A", 1, 'B', 2), -1, 6, 2), (2, 1, 2, 1))

    def test_index_o_behaving_like_index_list(self):
        self.assertEqual(["A", 1, 'B', 2].index("A"), 0)
        self.assertEqual(index_o(["A", 1, 'B', 2], "A"), 0)

        self.assertEqual(["A", 1, 'B', 2].index('B'), 2)
        self.assertEqual(index_o(["A", 1, 'B', 2], 'B'), 2)


        with self.assertRaises(ValueError):
            var = ["A", 1, 'B', 2].index(['B', 2])
        with self.assertRaises(ValueError):
            var = index_o(["A", 1, 'B', 2], ['B', 2])

    def test_index_o_behaving_like_index_tuple(self):
        self.assertEqual(("A", 1, 'B', 2).index("A"), 0)
        self.assertEqual(index_o(("A", 1, 'B', 2), "A"), 0)

        self.assertEqual(("A", 1, 'B', 2).index('B'), 2)
        self.assertEqual(index_o(("A", 1, 'B', 2), 'B'), 2)

        with self.assertRaises(ValueError):
            var = ("A", 1, 'B', 2).index(('B', 2))
        with self.assertRaises(ValueError):
            var = index_o(("A", 1, 'B', 2), ('B', 2))

    def test_index_o_behaving_like_index_str(self):
        self.assertEqual("ABCDE".index("B"), 1)
        self.assertEqual(index_o("ABCDE", "B"), 1)

        self.assertEqual("ABCDE".index("CD"), 2)
        self.assertEqual(index_o("ABCDE", "CD"), 2)

        with self.assertRaises(ValueError):
            var = "ABCDE".index("CA")
        with self.assertRaises(ValueError):
            var = index_o("ABCDE", "CA")

        self.assertEqual("ABCDE".index(""), 0)
        self.assertEqual(index_o("ABCDE", ""), 0)

        self.assertEqual("".index(""), 0)
        self.assertEqual(index_o("", ""), 0)

        with self.assertRaises(ValueError):
            var = "".index("A")
        with self.assertRaises(ValueError):
            var = index_o("", "A")

        self.assertEqual("ABCDE".index("E", 2), 4)
        self.assertEqual(index_o("ABCDE", "E", 2), 4)

        with self.assertRaises(ValueError):
            var = "ABCDE".index("E", 2, 4)
        with self.assertRaises(ValueError):
            var = index_o("ABCDE", "E", 2, 4)

        self.assertEqual("ABCDE".index("E", 2, 5), 4)
        self.assertEqual(index_o("ABCDE", "E", 2, 5), 4)

        with self.assertRaises(ValueError):
            "ABCDE".index("C", 2, 1)
        with self.assertRaises(ValueError):
            var = index_o("ABCDE", "C", 2, 1)

        self.assertEqual("ABCDE".index("B", -10, -2), 1)
        self.assertEqual(index_o("ABCDE", "B", -10, -2), 1)

    def test_take_while_o(self):
        self.assertEqual(take_while_o((0, 1, 2, 3, 4), lambda x: x < 3, 1), (1, 2))
        # wrap around the ring
        self.assertEqual(take_while_o((0, 1, 2, 3, 4), lambda x: x != 1, 3), (3, 4, 0))
        self.assertEqual(take_while_o("ABCDE", lambda c: c < "D"), "ABC")
        self.assertEqual(take_while_o((), lambda x: True), ())

    def test_drop_while_o(self):
        self.assertEqual(drop_while_o((0, 1, 2, 3, 4), lambda x: x < 3, 1), (3, 4, 0))
        self.assertEqual(drop_while_o("ABCDE", lambda c: c < "D"), "DE")
        self.assertEqual(drop_while_o((), lambda x: True), ())

    def test_span_o(self):
        self.assertEqual(span_o((0, 1, 2, 3, 4), lambda x: x < 3, 1), ((1, 2), (3, 4, 0)))
        # parts agree with take_while_o and drop_while_o
        prefix, suffix = span_o((1, 2, 3, 4, 5), lambda x: x < 4, 2)
        self.assertEqual(prefix, take_while_o((1, 2, 3, 4, 5), lambda x: x < 4, 2))
        self.assertEqual(suffix, drop_while_o((1, 2, 3, 4, 5), lambda x: x < 4, 2))

    def test_index_o_not_behaving_like_index(self):
        with self.assertRaises(ValueError):
            var = "ABCDE".index("A", -1)
        self.assertEqual(index_o("ABCDE", "A", -1), 0)

        with self.assertRaises(ValueError):
            var = "ABCDE".index("A", 5)
        self.assertEqual(index_o("ABCDE", "A", 5), 0)

        with self.assertRaises(ValueError):
            var = "ABCDE".index("A", -1, 6)
        self.assertEqual(index_o("ABCDE", "A", -1, 6), 0)

        with self.assertRaises(ValueError):
            var = "ABCDE".index("B", 2, 7)
        self.assertEqual(index_o("ABC", "B", 2, 7), 1)
        self.assertEqual(index_o("ABC", "BCA", 2, 7), 1)
        self.assertEqual(index_o("ABC", "BCAB", 2, 8), 1)
        self.assertEqual(index_o("ABCDE", "B", 2, 7), 1)


if __name__ == '__main__':
    unittest.main()
