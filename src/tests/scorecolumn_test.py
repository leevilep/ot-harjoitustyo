import unittest
from scorecolumn import ScoreColumn

class TestScoreColumn(unittest.TestCase):
    def setUp(self):
        self.sc = ScoreColumn("player name")

    def test_one_pair_score(self):
        self.assertEqual(self.sc.check_one_pair([5,3,5,2,3]), 10)

    def test_one_pair_zero(self):
        self.assertEqual(self.sc.check_one_pair([3,4,5,2,1]), 0)