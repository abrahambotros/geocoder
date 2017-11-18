"""
Tests for math utils.
"""

# External imports
import unittest

# Internal imports
from app.utils import math as utils_math


class TestMath(unittest.TestCase):

    def test_equalish(self):
        equalish = utils_math.equalish
        self.assertTrue(equalish(0, 0))
        self.assertFalse(equalish(0, 1))
        self.assertTrue(equalish(x=0.55555, y=0.55556, precision_digits=6))
        self.assertFalse(equalish(x=0.55555, y=0.55556, precision_digits=5))
