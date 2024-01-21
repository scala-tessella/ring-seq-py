import unittest

from ring_seq import rotational_symmetry, symmetry, symmetry_indices
from examples.Ring import Ring


class RingOps(unittest.TestCase):

    def setUp(self):
        self.seq = [1, 2, 3, 4]
        self.ring = Ring(self.seq)

    def test_creation(self):
        self.assertEqual(self.ring.current_head(), 1)
        self.assertEqual(self.ring.head_index, 0)
        self.assertEqual(self.ring.is_reflected, False)
        self.assertEqual(self.ring.current(), self.seq)


if __name__ == '__main__':
    unittest.main()
