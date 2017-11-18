"""
Tests for Google Maps third-party controller.
"""

# External imports
import unittest

# Internal imports
from app.controllers.tests.utils import ADDRESS_TO_LATLNG_DICT
from app.controllers.third_party import google_maps as gmaps_controller


class TestGoogleMaps(unittest.TestCase):

    def test_geocode(self):
        for address, lat_lng in ADDRESS_TO_LATLNG_DICT.items():
            result = gmaps_controller.geocode(address=address)
            self.assertTrue(result == lat_lng,
                            "Result (%s) not equal to expected LatLng (%s) for address: %s" % (result, lat_lng, address))
