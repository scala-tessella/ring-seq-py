import unittest
import ring

from typing import Any


class IndexingOps(unittest.TestCase):

    def test_index_from(self):
        self.assertEqual(ring.index_from(-1, "ABCDE"), 4)
        self.assertEqual(ring.index_from(5, "ABCDE"), 0)
        self.assertEqual(ring.index_from(-1, ["A", 1, 'B', 2]), 3)
        self.assertEqual(ring.index_from(-1, ("A", 1, 'B', 2)), 3)
        with self.assertRaises(ArithmeticError):
            ring.index_from(0, [])

    def test_apply_o(self):
        self.assertEqual(ring.apply_o(-1, "ABCDE"), "E")
        self.assertEqual(ring.apply_o(5, "ABCDE"), "A")
        self.assertEqual("ABCDE"[-1], "E")
        with self.assertRaises(IndexError):
            var: str = "ABCDE"[-6]
        with self.assertRaises(IndexError):
            var: str = "ABCDE"[5]
        with self.assertRaises(ArithmeticError):
            ring.apply_o(0, [])
        with self.assertRaises(IndexError):
            var: Any = [][0]


if __name__ == '__main__':
    unittest.main()
