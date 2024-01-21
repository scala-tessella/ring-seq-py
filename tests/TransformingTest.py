import unittest

from ring_seq import rotate_left, rotate_right, start_at, reflect_at


class TransformingOps(unittest.TestCase):

    def test_rotate_right(self):
        self.assertEqual(rotate_right("ABCDE", 0), "ABCDE")
        self.assertEqual(rotate_right("ABCDE", 1), "EABCD")
        self.assertEqual(rotate_right("ABCDE", 6), "EABCD")
        self.assertEqual(rotate_right("ABCDE", -4), "EABCD")
        self.assertEqual(rotate_right(["A", 1, 'B', 2], 3), [1, 'B', 2, "A"])
        self.assertEqual(rotate_right(("A", 1, 'B', 2), -1), (1, 'B', 2, "A"))

    def test_rotate_left(self):
        self.assertEqual(rotate_left("ABCDE", 0), "ABCDE")
        self.assertEqual(rotate_left("ABCDE", 1), "BCDEA")
        self.assertEqual(rotate_left("ABCDE", 6), "BCDEA")
        self.assertEqual(rotate_left("ABCDE", -4), "BCDEA")
        self.assertEqual(rotate_left(["A", 1, 'B', 2], 3), [2, "A", 1, 'B'])
        self.assertEqual(rotate_left(("A", 1, 'B', 2), -1), (2, "A", 1, 'B'))

    def test_start_at(self):
        self.assertEqual(start_at("ABCDE", 0), "ABCDE")
        self.assertEqual(start_at("ABCDE", 1), "BCDEA")
        self.assertEqual(start_at("ABCDE", 6), "BCDEA")

    def test_reflect_at(self):
        self.assertEqual(reflect_at("ABCDE", 0), "AEDCB")
        self.assertEqual(reflect_at(["A", 1, 'B', 2], 0), ["A", 2, 'B', 1])
        self.assertEqual(reflect_at(("A", 1, 'B', 2), 0), ("A", 2, 'B', 1))


if __name__ == '__main__':
    unittest.main()
