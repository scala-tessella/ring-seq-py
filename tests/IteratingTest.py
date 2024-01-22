import unittest

from ring_seq.methods import reflections, reversions, rotations, rotations_and_reflections


class IteratingOps(unittest.TestCase):

    def test_rotations(self):
        self.assertEqual(list(rotations("ABCDE")), ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"])

    def test_reflections(self):
        self.assertEqual(list(reflections("ABCDE")), ["ABCDE", "AEDCB"])

    def test_reversions(self):
        self.assertEqual(list(reversions("ABCDE")), ["ABCDE", "EDCBA"])

    def test_rotations_and_reflections(self):
        self.assertEqual(
            list(rotations_and_reflections("ABCDE")),
            [
                "ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD",
                "AEDCB", "EDCBA", "DCBAE", "CBAED", "BAEDC"
            ]
        )


if __name__ == '__main__':
    unittest.main()
