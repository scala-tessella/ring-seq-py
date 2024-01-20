import unittest

from IndexingTest import IndexingOps
from SlicingTest import SlicingOps
from TransformingTest import TransformingOps
from IteratingTest import IteratingOps


class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter((IndexingOps, SlicingOps, TransformingOps, IteratingOps)))


if __name__ == '__main__':
    unittest.main()
