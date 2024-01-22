import unittest

from ring_seq.methods import is_reflection_of, is_reversion_of, is_rotation_of, is_rotation_or_reflection_of


class ComparingOps(unittest.TestCase):

    def test_is_rotation_of(self):
        self.assertTrue(is_rotation_of("ABCDE", "CDEAB"))

    def test_is_reflection_of(self):
        self.assertTrue(is_reflection_of("ABCDE", "AEDCB"))

    def test_is_reversion_of(self):
        self.assertTrue(is_reversion_of("ABCDE", "EDCBA"))

    def test_is_rotation_or_reflection_of(self):
        self.assertTrue(is_rotation_or_reflection_of("ABCDE", "CBAED"))


if __name__ == '__main__':
    unittest.main()
