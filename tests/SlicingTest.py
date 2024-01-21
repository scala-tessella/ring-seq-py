import unittest

from ring_seq import slice_o


class SlicingOps(unittest.TestCase):

    def test_slicing_o(self):
        self.assertEqual(slice_o("ABCDE", -1, 6), "EABCDEA")
        self.assertEqual(slice_o("ABCDE", 1, 3), "BC")
        self.assertEqual("ABCDE"[1:3], "BC")
        self.assertEqual(slice_o("ABCDE", 3, 3), "")
        self.assertEqual(slice_o("ABCDE", 4, 3), "")


if __name__ == '__main__':
    unittest.main()
