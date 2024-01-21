import unittest

from ring_seq import index_from, apply_o
from typing import Any


class IndexingOps(unittest.TestCase):

    def test_index_from(self):
        self.assertEqual(index_from("ABCDE", -1), 4)
        self.assertEqual(index_from("ABCDE", 5), 0)
        self.assertEqual(index_from(["A", 1, 'B', 2], -1), 3)
        self.assertEqual(index_from(("A", 1, 'B', 2), -1), 3)
        with self.assertRaises(ArithmeticError):
            index_from([], 0)

    def test_apply_o(self):
        self.assertEqual(apply_o("ABCDE", -1), "E")
        self.assertEqual(apply_o("ABCDE", 5), "A")
        self.assertEqual("ABCDE"[-1], "E")
        with self.assertRaises(IndexError):
            var: str = "ABCDE"[-6]
        with self.assertRaises(IndexError):
            var: str = "ABCDE"[5]
        with self.assertRaises(ArithmeticError):
            apply_o([], 0)
        with self.assertRaises(IndexError):
            var: Any = [][0]


if __name__ == '__main__':
    unittest.main()
