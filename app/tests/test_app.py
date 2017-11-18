"""
Tests for highest level of app - server, routes, primary endpoints, etc.
"""

# External imports
import json
import unittest
from urllib.parse import urlencode

# Internal imports
from app import app
from app.controllers.tests.utils import ADDRESS_TO_LATLNG_DICT
from app.models.lat_lng import LatLng


class TestApp(unittest.TestCase):

    def setUp(self):
        self.test_client = app.SERVER.test_client()

    def tearDown(self):
        self.test_client = None

    def test_flask_app_exists(self):
        self.assertTrue(app.SERVER)

    def test_get_test_client(self):
        self.assertTrue(self.test_client)

    def test_route_root(self):
        # For each address-LatLng test case:
        for address, lat_lng in ADDRESS_TO_LATLNG_DICT.items():
            # Make request containing this address as URL param. Send to root
            # route on this Flask server app instance via test client.
            # TODO: Move "address" out to constant str.
            resp = self.test_client.get("/?%s" % urlencode({
                "address": address,
            }))
            resp_data = json.loads(resp.data)

            # Check response.
            expected_dict = {
                LatLng.API_FIELD_LAT: lat_lng.lat,
                LatLng.API_FIELD_LNG: lat_lng.lng,
            }
            # TODO: Use constant-str keys.
            self.assertTrue(resp_data == expected_dict,
                            "Response data dict (%s) should match expected simple dict (%s)" % (resp_data, expected_dict))  # NOQA: E501
