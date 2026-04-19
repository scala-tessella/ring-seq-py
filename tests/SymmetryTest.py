import unittest

from ring_seq import Edge, RingSeq, Vertex


class SymmetryOps(unittest.TestCase):

    def setUp(self):
        self.spin3 = RingSeq((1, 2, 3, 1, 2, 3, 1, 2, 3))
        self.eptagon = RingSeq((6, 6, 6, 6, 6, 6, 6))
        self.squaroid = RingSeq((2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2))
        self.axis_on_element = RingSeq((1, 2, 3, 4, 3, 2))
        self.axis_off_element = RingSeq((1, 2, 3, 4, 4, 3, 2, 1))
        self.axis_on_off_element = RingSeq((1, 2, 3, 4, 4, 3, 2))

    def test_rotational_symmetry(self):
        self.assertEqual(RingSeq("ABCDE").rotational_symmetry(), 1)
        self.assertEqual(RingSeq([]).rotational_symmetry(), 1)
        self.assertEqual(self.spin3.rotational_symmetry(), 3)
        self.assertEqual(self.eptagon.rotational_symmetry(), 7)
        self.assertEqual(self.squaroid.rotational_symmetry(), 4)
        self.assertEqual(self.axis_on_element.rotational_symmetry(), 1)
        self.assertEqual(self.axis_off_element.rotational_symmetry(), 1)
        self.assertEqual(self.axis_on_off_element.rotational_symmetry(), 1)

    def test_symmetry_indices(self):
        self.assertEqual(RingSeq("ABCDE").symmetry_indices(), [])
        self.assertEqual(RingSeq([]).symmetry_indices(), [])
        self.assertEqual(self.spin3.symmetry_indices(), [])
        self.assertEqual(self.eptagon.symmetry_indices(), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(self.squaroid.symmetry_indices(), [0, 3, 6, 9])
        self.assertEqual(self.axis_on_element.symmetry_indices(), [5])
        self.assertEqual(self.axis_off_element.symmetry_indices(), [0])
        self.assertEqual(self.axis_on_off_element.symmetry_indices(), [6])

    def test_symmetry(self):
        self.assertEqual(RingSeq("ABCDE").symmetry(), 0)
        self.assertEqual(RingSeq([]).symmetry(), 0)
        self.assertEqual(self.spin3.symmetry(), 0)
        self.assertEqual(self.eptagon.symmetry(), 7)
        self.assertEqual(self.squaroid.symmetry(), 4)
        self.assertEqual(self.axis_on_element.symmetry(), 1)
        self.assertEqual(self.axis_off_element.symmetry(), 1)
        self.assertEqual(self.axis_on_off_element.symmetry(), 1)

    def test_reflectional_symmetry_axes_triangle(self):
        self.assertEqual(
            RingSeq((1, 1, 1)).reflectional_symmetry_axes(),
            [
                (Vertex(1), Edge(2, 3)),
                (Vertex(2), Edge(0, 3)),
                (Vertex(0), Edge(1, 3)),
            ],
        )

    def test_reflectional_symmetry_axes_doubled_triangle(self):
        self.assertEqual(
            RingSeq((1, 2, 1, 2, 1, 2)).reflectional_symmetry_axes(),
            [
                (Vertex(2), Vertex(5)),
                (Vertex(1), Vertex(4)),
                (Vertex(0), Vertex(3)),
            ],
        )

    def test_reflectional_symmetry_axes_square(self):
        self.assertEqual(
            RingSeq((1, 1, 1, 1)).reflectional_symmetry_axes(),
            [
                (Edge(1, 4), Edge(3, 4)),
                (Vertex(1), Vertex(3)),
                (Edge(0, 4), Edge(2, 4)),
                (Vertex(0), Vertex(2)),
            ],
        )

    def test_reflectional_symmetry_axes_doubled_square(self):
        self.assertEqual(
            RingSeq((1, 2, 1, 2, 1, 2, 1, 2)).reflectional_symmetry_axes(),
            [
                (Vertex(3), Vertex(7)),
                (Vertex(2), Vertex(6)),
                (Vertex(1), Vertex(5)),
                (Vertex(0), Vertex(4)),
            ],
        )

    def test_reflectional_symmetry_axes_specular_pentagon(self):
        self.assertEqual(
            RingSeq((1, 1, 2, 3, 2)).reflectional_symmetry_axes(),
            [(Vertex(3), Edge(0, 5))],
        )

    def test_edge_computes_second_endpoint(self):
        e = Edge(2, 4)
        self.assertEqual(e.i, 2)
        self.assertEqual(e.j, 3)
        self.assertEqual(Edge(3, 4).j, 0)

    def test_edge_normalizes_out_of_range_i(self):
        self.assertEqual(Edge(-1, 5), Edge(4, 5))
        self.assertEqual(Edge(7, 5), Edge(2, 5))

    def test_edge_rejects_non_positive_ring_size(self):
        with self.assertRaises(ValueError):
            Edge(0, 0)
        with self.assertRaises(ValueError):
            Edge(0, -1)

    def test_edge_supports_pattern_matching(self):
        match Edge(2, 4):
            case Edge(i, j):
                self.assertEqual(i, 2)
                self.assertEqual(j, 3)


if __name__ == "__main__":
    unittest.main()
