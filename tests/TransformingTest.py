import unittest

from ring_seq import rotate_left, rotate_right, start_at, reflect_at


class TransformingOps(unittest.TestCase):

    def test_rotate_right(self):
        self.assertEqual(rotate_right(0, "ABCDE"), "ABCDE")
        self.assertEqual(rotate_right(1, "ABCDE"), "EABCD")
        self.assertEqual(rotate_right(6, "ABCDE"), "EABCD")
        self.assertEqual(rotate_right(-4, "ABCDE"), "EABCD")
        self.assertEqual(rotate_right(3, ["A", 1, 'B', 2]), [1, 'B', 2, "A"])
        self.assertEqual(rotate_right(-1, ("A", 1, 'B', 2)), (1, 'B', 2, "A"))

    def test_rotate_left(self):
        self.assertEqual(rotate_left(0, "ABCDE"), "ABCDE")
        self.assertEqual(rotate_left(1, "ABCDE"), "BCDEA")
        self.assertEqual(rotate_left(6, "ABCDE"), "BCDEA")
        self.assertEqual(rotate_left(-4, "ABCDE"), "BCDEA")
        self.assertEqual(rotate_left(3, ["A", 1, 'B', 2]), [2, "A", 1, 'B'])
        self.assertEqual(rotate_left(-1, ("A", 1, 'B', 2)), (2, "A", 1, 'B'))

    def test_start_at(self):
        self.assertEqual(start_at(0, "ABCDE"), "ABCDE")
        self.assertEqual(start_at(1, "ABCDE"), "BCDEA")
        self.assertEqual(start_at(6, "ABCDE"), "BCDEA")

    def test_reflect_at(self):
        self.assertEqual(reflect_at(0, "ABCDE"), "AEDCB")
        self.assertEqual(reflect_at(0, ["A", 1, 'B', 2]), ["A", 2, 'B', 1])
        self.assertEqual(reflect_at(0, ("A", 1, 'B', 2)), ("A", 2, 'B', 1))


if __name__ == '__main__':
    unittest.main()
