import unittest
from timer import Timer

class TestTimer(unittest.TestCase):
    def setUp(self):
        self.t = Timer()
    def test_start_and_stop_return_values(self):
        assert not self.t.stop()
        assert self.t.start()
        assert not self.t.start()
        assert self.t.stop()
        assert not self.t.stop()
