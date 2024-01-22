import unittest

from ring_seq.examples.Ring import Ring


class RingOps(unittest.TestCase):

    def setUp(self):
        self.seq = [1, 2, 3, 4]
        self.ring = Ring(self.seq)

    def test_creation(self):
        self.assertEqual(self.ring.head_index, 0)
        self.assertEqual(self.ring.is_reflected, False)
        self.assertEqual(self.ring.current_head(), 1)
        self.assertEqual(self.ring.current(), self.seq)

    def test_rotation_1_step_right(self):
        self.ring.rotate_r(1)
        self.assertEqual(self.ring.head_index, -1)
        self.assertEqual(self.ring.is_reflected, False)
        self.assertEqual(self.ring.current_head(), 4)
        self.assertEqual(self.ring.current(), [4, 1, 2, 3])

    def test_rotation_back_1_step_left(self):
        self.ring.rotate_r(1)
        self.ring.rotate_l(1)
        self.assertEqual(self.ring.head_index, 0)
        self.assertEqual(self.ring.is_reflected, False)
        self.assertEqual(self.ring.current_head(), 1)
        self.assertEqual(self.ring.current(), self.seq)

    def test_reflection(self):
        self.ring.reflect()
        self.assertEqual(self.ring.head_index, 0)
        self.assertEqual(self.ring.is_reflected, True)
        self.assertEqual(self.ring.current_head(), 1)
        self.assertEqual(self.ring.current(), [1, 4, 3, 2])

    def test_reflection_plus_1_step_right(self):
        self.ring.reflect()
        self.ring.rotate_r(1)
        self.assertEqual(self.ring.head_index, 1)
        self.assertEqual(self.ring.is_reflected, True)
        self.assertEqual(self.ring.current_head(), 2)
        self.assertEqual(self.ring.current(), [2, 1, 4, 3])

    def test_reflection_plus_1_step_right_plus_reflection(self):
        self.ring.reflect()
        self.ring.rotate_r(1)
        self.ring.reflect()
        self.assertEqual(self.ring.head_index, 1)
        self.assertEqual(self.ring.is_reflected, False)
        self.assertEqual(self.ring.current_head(), 2)
        self.assertEqual(self.ring.current(), [2, 3, 4, 1])

    def test_reflection_plus_1_step_right_plus_reflection_plus_1_step_left(self):
        self.ring.reflect()
        self.ring.rotate_r(1)
        self.ring.reflect()
        self.ring.rotate_r(1)
        self.assertEqual(self.ring.head_index, 0)
        self.assertEqual(self.ring.is_reflected, False)
        self.assertEqual(self.ring.current_head(), 1)
        self.assertEqual(self.ring.current(), self.seq)


if __name__ == '__main__':
    unittest.main()
