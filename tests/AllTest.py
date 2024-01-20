import unittest

from IndexingTest import IndexingOps
from SlicingTest import SlicingOps
from TransformingTest import TransformingOps
from IteratingTest import IteratingOps
from ComparingTest import ComparingOps
from SymmetryTest import SymmetryOps

class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter((IndexingOps, SlicingOps, TransformingOps, IteratingOps, ComparingOps, SymmetryOps)))


if __name__ == '__main__':
    unittest.main()
