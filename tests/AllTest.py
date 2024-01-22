import unittest

from IndexingTest import IndexingOps
from SlicingTest import SlicingOps
from TransformingTest import TransformingOps
from IteratingTest import IteratingOps
from ComparingTest import ComparingOps
from SymmetryTest import SymmetryOps
from RingSeqTest import RingSeqOps
from examples.RingTest import RingOps


class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter(
            (IndexingOps, SlicingOps, TransformingOps, IteratingOps, ComparingOps, SymmetryOps, RingOps, RingSeqOps)
        ))


if __name__ == '__main__':
    unittest.main()
