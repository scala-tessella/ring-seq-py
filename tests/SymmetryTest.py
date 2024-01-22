import unittest

from ring_seq.methods import rotational_symmetry, symmetry, symmetry_indices


class SymmetryOps(unittest.TestCase):

    def setUp(self):
        self.spin3: tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)
        self.eptagon: tuple = (6, 6, 6, 6, 6, 6, 6)
        self.squaroid: tuple = (2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2)
        self.axisOnElement: tuple = (1, 2, 3, 4, 3, 2)
        self.axisOffElement: tuple = (1, 2, 3, 4, 4, 3, 2, 1)
        self.axisOnOffElement: tuple = (1, 2, 3, 4, 4, 3, 2)

    def test_rotational_symmetry(self):
        self.assertEqual(rotational_symmetry("ABCDE"), 1)
        self.assertEqual(rotational_symmetry([]), 1)
        self.assertEqual(rotational_symmetry(self.spin3), 3)
        self.assertEqual(rotational_symmetry(self.eptagon), 7)
        self.assertEqual(rotational_symmetry(self.squaroid), 4)
        self.assertEqual(rotational_symmetry(self.axisOnElement), 1)
        self.assertEqual(rotational_symmetry(self.axisOffElement), 1)
        self.assertEqual(rotational_symmetry(self.axisOnOffElement), 1)

    def test_symmetry_indices(self):
        self.assertEqual(symmetry_indices("ABCDE"), [])
        self.assertEqual(symmetry_indices([]), [])
        self.assertEqual(symmetry_indices(self.spin3), [])
        self.assertEqual(symmetry_indices(self.eptagon), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(symmetry_indices(self.squaroid), [1, 4, 7, 10])
        self.assertEqual(symmetry_indices(self.axisOnElement), [0])
        self.assertEqual(symmetry_indices(self.axisOffElement), [3])
        self.assertEqual(symmetry_indices(self.axisOnOffElement), [0])

    def test_symmetry(self):
        self.assertEqual(symmetry("ABCDE"), 0)
        self.assertEqual(symmetry([]), 0)
        self.assertEqual(symmetry(self.spin3), 0)
        self.assertEqual(symmetry(self.eptagon), 7)
        self.assertEqual(symmetry(self.squaroid), 4)
        self.assertEqual(symmetry(self.axisOnElement), 1)
        self.assertEqual(symmetry(self.axisOffElement), 1)
        self.assertEqual(symmetry(self.axisOnOffElement), 1)


if __name__ == '__main__':
    unittest.main()
