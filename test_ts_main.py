from unittest import TestCase
from ts_main import Ts

class TestTs(TestCase):
    def setUp(self):
        self.Ts = Ts()

    def test_accelerate(self):
        self.Ts.accelerate()
        self.assertEqual(self.Ts.speed, 5)

    def test_step(self):
        self.Ts.accelerate()
        self.assertEqual(self.Ts.speed, 5)
