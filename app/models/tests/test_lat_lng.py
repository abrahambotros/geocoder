"""
Tests for the LatLng model.
"""

# External imports
import unittest

# Internal imports
from app.models.lat_lng import LatLng


class TestLatLng(unittest.TestCase):

    def test_create(self):
        self.assertTrue(LatLng(0.0, 1.0))
