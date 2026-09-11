import unittest
from clock_backend import Clock
from clock_backend import clock_testing

class TestClockInputs(unittest.TestCase):
    def test_24_format(self):
        self.assertTrue(clock_testing(Clock(22,0,0)))
        self.assertFalse(clock_testing(Clock(55,0,0)))
        self.assertFalse(clock_testing(Clock(-1,0,0)))

    def test_12_format(self):
        self.assertTrue(clock_testing(Clock(12,10,30,False)))
        self.assertFalse(clock_testing(Clock(13,30,0,False)))
        self.assertFalse(clock_testing(Clock(0,0,0,False,)))
        self.assertFalse(clock_testing(Clock(-1,0,0,False)))

    def test_minutes(self):
        self.assertTrue(clock_testing(Clock(0,50,0)))
        self.assertFalse(clock_testing(Clock(0,60,0)))
        self.assertFalse(clock_testing(Clock(0,-10,0)))

    def test_seconds(self):
        self.assertTrue(clock_testing(Clock(0,0,59)))
        self.assertFalse(clock_testing(Clock(0,0,60)))
        self.assertFalse(clock_testing(Clock(0,0,-15)))

if __name__ == '__main__':
    unittest.main()