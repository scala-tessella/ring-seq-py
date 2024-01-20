import unittest

from ring_seq import reflections, reversions


class IteratingOps(unittest.TestCase):

    def test_reflections(self):
        self.assertEqual(list(reflections("ABCDE")), ["ABCDE", "AEDCB"])

    def test_reversions(self):
        self.assertEqual(list(reversions("ABCDE")), ["ABCDE", "EDCBA"])

if __name__ == '__main__':
    unittest.main()
