import unittest
import ring


class TransformingOps(unittest.TestCase):

    def test_rotate_right(self):
        self.assertEqual(ring.rotate_right(0, "ABCDE"), "ABCDE")
        self.assertEqual(ring.rotate_right(1, "ABCDE"), "EABCD")
        self.assertEqual(ring.rotate_right(6, "ABCDE"), "EABCD")
        self.assertEqual(ring.rotate_right(-4, "ABCDE"), "EABCD")
        self.assertEqual(ring.rotate_right(3, ["A", 1, 'B', 2]), [1, 'B', 2, "A"])
        self.assertEqual(ring.rotate_right(-1, ("A", 1, 'B', 2)), (1, 'B', 2, "A"))

    def test_rotate_left(self):
        self.assertEqual(ring.rotate_left(0, "ABCDE"), "ABCDE")
        self.assertEqual(ring.rotate_left(1, "ABCDE"), "BCDEA")
        self.assertEqual(ring.rotate_left(6, "ABCDE"), "BCDEA")
        self.assertEqual(ring.rotate_left(-4, "ABCDE"), "BCDEA")
        self.assertEqual(ring.rotate_left(3, ["A", 1, 'B', 2]), [2, "A", 1, 'B'])
        self.assertEqual(ring.rotate_left(-1, ("A", 1, 'B', 2)), (2, "A", 1, 'B'))

    def test_start_at(self):
        self.assertEqual(ring.start_at(0, "ABCDE"), "ABCDE")
        self.assertEqual(ring.start_at(1, "ABCDE"), "BCDEA")
        self.assertEqual(ring.start_at(6, "ABCDE"), "BCDEA")

    def test_typed_reverse(self):
        with self.assertRaises(AttributeError):
            ring.__typed_reverse("ABCDE")

    def test_reflect_at(self):
        self.assertEqual(ring.reflect_at(0, "ABCDE"), "AEDCB")
        self.assertEqual(ring.reflect_at(0, ["A", 1, 'B', 2]), ["A", 2, 'B', 1])
        self.assertEqual(ring.reflect_at(0, ("A", 1, 'B', 2)), ("A", 2, 'B', 1))


if __name__ == '__main__':
    unittest.main()
