"""
Tests for here third-party controller.
"""

# External imports
import unittest

# Internal imports
from app.controllers.tests.utils import ADDRESS_TO_LATLNG_DICT
from app.controllers.third_party import here as here_controller


class TestHere(unittest.TestCase):

    def test_geocode(self):
        for address, lat_lng in ADDRESS_TO_LATLNG_DICT.items():
            result = here_controller.geocode(address=address)
            self.assertTrue(result == lat_lng,
                            "Result not equal to expected LatLng")
