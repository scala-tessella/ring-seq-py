import unittest

from ring_seq import slice_o


class SlicingOps(unittest.TestCase):

    def test_slicing_o(self):
        self.assertEqual(slice_o(-1, 6, "ABCDE"), "EABCDEA")
        self.assertEqual(slice_o(1, 3, "ABCDE"), "BC")
        self.assertEqual("ABCDE"[1:3], "BC")
        self.assertEqual(slice_o(3, 3, "ABCDE"), "")
        self.assertEqual(slice_o(4, 3, "ABCDE"), "")


if __name__ == '__main__':
    unittest.main()
