import unittest

from ring_seq import rotational_symmetry


class SymmetryOps(unittest.TestCase):

    def setUp(self):
        self.spin3: tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)
        self.eptagon: tuple = (6, 6, 6, 6, 6, 6, 6)
        self.squaroid: tuple = (2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2)
        self.axisOnElement: tuple = (1, 2, 3, 4, 3, 2)
        self.axisOffElement: tuple = (1, 2, 3, 4, 4, 3, 2, 1)
        self.axisOnOffElement: tuple = (1, 2, 3, 4, 4, 3, 2)

    def test_rotational_symmetry(self):
        # self.assertEqual(rotational_symmetry("ABCDE"), 1)
        # self.assertEqual(rotational_symmetry([]), 1)
        self.assertEqual(rotational_symmetry(self.spin3), 3)
        self.assertEqual(rotational_symmetry(self.eptagon), 7)
        self.assertEqual(rotational_symmetry(self.squaroid), 4)
        self.assertEqual(rotational_symmetry(self.axisOnElement), 1)
        self.assertEqual(rotational_symmetry(self.axisOffElement), 1)
        self.assertEqual(rotational_symmetry(self.axisOnOffElement), 1)


if __name__ == '__main__':
    unittest.main()
