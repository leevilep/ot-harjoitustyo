import unittest
from scorecolumn import ScoreColumn


class TestScoreColumn(unittest.TestCase):
    def setUp(self):
        self.sc = ScoreColumn("player name")

    def test_one_pair_score(self):
        self.assertEqual(self.sc.check_one_pair([5, 3, 5, 2, 3]), 10)

    def test_one_pair_zero(self):
        self.assertEqual(self.sc.check_one_pair([3, 4, 5, 2, 1]), 0)

    def test_two_pairs_score(self):
        self.assertEqual(self.sc.check_two_pairs([2, 3, 5, 2, 3]), 10)

    def test_two_pairs_zero(self):
        self.assertEqual(self.sc.check_two_pairs([4, 4, 4, 4, 1]), 0)

    def test_three_of_a_kind_score(self):
        self.assertEqual(self.sc.check_three_of_a_kind([4,2,3,4,4]), 12)

    def test_three_of_a_kind_zero(self):
        self.assertEqual(self.sc.check_three_of_a_kind([4,2,6,4,6]), 0)

    def test_four_of_a_kind_score(self):
        self.assertEqual(self.sc.check_four_of_a_kind([2,3,2,2,2]), 8)

    def test_four_of_a_kind_zero(self):
        self.assertEqual(self.sc.check_four_of_a_kind([3,4,3,3,4]), 0)