import unittest

from ring_seq.methods import reflections, reversions, rotations, rotations_and_reflections


class IteratingOps(unittest.TestCase):

    def test_rotations(self):
        self.assertEqual(list(rotations([])), [])
        self.assertEqual(list(rotations("")), [])
        self.assertEqual(list(rotations(())), [])
        self.assertEqual(list(rotations("ABCDE")), ["ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"])

    def test_reflections(self):
        self.assertEqual(list(reflections([])), [])
        self.assertEqual(list(reflections("")), [])
        self.assertEqual(list(reflections(())), [])
        self.assertEqual(list(reflections("ABCDE")), ["ABCDE", "AEDCB"])

    def test_reversions(self):
        self.assertEqual(list(reversions([])), [])
        self.assertEqual(list(reversions("")), [])
        self.assertEqual(list(reversions(())), [])
        self.assertEqual(list(reversions("ABCDE")), ["ABCDE", "EDCBA"])
        self.assertEqual(list(reversions(["A", 1, 'B', 2])), [["A", 1, 'B', 2], [2, "B", 1, 'A']])
        self.assertEqual(list(reversions(("A", 1, 'B', 2))), [("A", 1, 'B', 2), (2, "B", 1, 'A')])

    def test_rotations_and_reflections(self):
        self.assertEqual(list(rotations_and_reflections([])), [])
        self.assertEqual(list(rotations_and_reflections("")), [])
        self.assertEqual(list(rotations_and_reflections(())), [])
        self.assertEqual(
            list(rotations_and_reflections("ABCDE")),
            [
                "ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD",
                "AEDCB", "EDCBA", "DCBAE", "CBAED", "BAEDC"
            ]
        )
        self.assertEqual(
            list(rotations_and_reflections(("A", 1, 'B', 2))),
            [
                ('A', 1, 'B', 2), (1, 'B', 2, 'A'),  ('B', 2, 'A', 1),  (2, 'A', 1, 'B'),
                ('A', 2, 'B', 1), (2, 'B', 1, 'A'),  ('B', 1, 'A', 2),  (1, 'A', 2, 'B')
            ]
        )


if __name__ == '__main__':
    unittest.main()
