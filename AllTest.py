import unittest

from TransformingTest import TransformingOps
from IndexingTest import IndexingOps


class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter(IndexingOps, TransformingOps))

if __name__ == '__main__':
    unittest.main()
