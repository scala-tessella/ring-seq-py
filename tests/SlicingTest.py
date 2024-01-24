import unittest

from ring_seq.methods import slice_o


class SlicingOps(unittest.TestCase):

    def test_slicing_o(self):
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


if __name__ == '__main__':
    unittest.main()
