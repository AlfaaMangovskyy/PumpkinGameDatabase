import unittest
from pumpkin_classes import *
import random as r

class PumpkinTestCase(unittest.TestCase):
    def test_golden_randomising(self):
        x = []
        for i in range(2000):
            b = 1 <= r.randint(1, round(shop["goldenrates"]*345)) <= 345
            x.append(b)
        self.assertNotIn(False, x)
    def test_graphics_finding(self):
        x = 0
        graphics = []
        while True:
            try:
                if not f"crate_casual_{x}.txt" in os.listdir("graphics"): break
                file = open(f"graphics/crate_casual_{x}.txt", "r", encoding="utf-8")
                g = file.read()
                graphics.append(g)
                x += 1
                file.close()
            except:
                break
        self.assertNotEqual(graphics, [])
unittest.main()