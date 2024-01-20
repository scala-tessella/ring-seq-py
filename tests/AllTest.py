import unittest

from IndexingTest import IndexingOps
from SlicingTest import SlicingOps
from TransformingTest import TransformingOps


class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter((IndexingOps, SlicingOps, TransformingOps)))


if __name__ == '__main__':
    unittest.main()
