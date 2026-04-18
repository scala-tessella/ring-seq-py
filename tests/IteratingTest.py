import unittest

from ring_seq.methods import (
    grouped_o,
    reflections,
    reversions,
    rotations,
    rotations_and_reflections,
    zip_with_index_o,
)


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


    def test_grouped_o(self):
        self.assertEqual(list(grouped_o("ABCDE", 2)), ["AB", "CD", "EA", "BC", "DE"])
        self.assertEqual(list(grouped_o("", 2)), [])
        self.assertEqual(list(grouped_o((), 3)), [])
        self.assertEqual(
            list(grouped_o((0, 1, 2, 3, 4), 3)),
            [(0, 1, 2), (3, 4, 0), (1, 2, 3), (4, 0, 1), (2, 3, 4)],
        )

    def test_zip_with_index_o(self):
        self.assertEqual(
            list(zip_with_index_o(("a", "b", "c"), 1)),
            [("b", 1), ("c", 2), ("a", 0)],
        )
        self.assertEqual(
            list(zip_with_index_o(("a", "b", "c"))),
            [("a", 0), ("b", 1), ("c", 2)],
        )
        self.assertEqual(list(zip_with_index_o(())), [])


if __name__ == '__main__':
    unittest.main()
