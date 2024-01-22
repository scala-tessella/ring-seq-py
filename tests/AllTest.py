import unittest

from tests.IndexingTest import IndexingOps
from tests.SlicingTest import SlicingOps
from tests.TransformingTest import TransformingOps
from tests.IteratingTest import IteratingOps
from tests.ComparingTest import ComparingOps
from tests.SymmetryTest import SymmetryOps
from tests.RingSeqTest import RingSeqOps
from tests.examples.RingTest import RingOps


class RingTestSuite(unittest.TestSuite):
    def test_all(self):
        self.addTests(iter(
            (IndexingOps, SlicingOps, TransformingOps, IteratingOps, ComparingOps, SymmetryOps, RingOps, RingSeqOps)
        ))


if __name__ == '__main__':
    unittest.main()
