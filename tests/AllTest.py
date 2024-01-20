import unittest

from IndexingTest import IndexingOps
from SlicingTest import SlicingOps
from TransformingTest import TransformingOps
from IteratingTest import IteratingOps
from ComparingTest import ComparingOps


class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter((IndexingOps, SlicingOps, TransformingOps, IteratingOps, ComparingOps)))


if __name__ == '__main__':
    unittest.main()
