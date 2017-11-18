"""
Tests for main controller.
"""

# External imports
import unittest

# Internal imports
from app.controllers.tests.utils import ADDRESS_TO_LATLNG_DICT
from app.controllers import main as main_controller


class TestMain(unittest.TestCase):

    def test_geocode(self):
        for address, lat_lng in ADDRESS_TO_LATLNG_DICT.items():
            result = main_controller.geocode(address=address)
            self.assertTrue(result == lat_lng,
                            "Result not equal to expected LatLng")

    def test_geocode_errors(self):
        for invalid_address in ["", None, 10]:
            with self.assertRaises(RuntimeError):
                main_controller.geocode(address=invalid_address)
