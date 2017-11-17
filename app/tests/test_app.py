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


class TestApp(unittest.TestCase):

    def setUp(self):
        self.test_client = app.APP.test_client()

    def tearDown(self):
        self.test_client = None

    def test_flask_app_exists(self):
        self.assertTrue(app.APP)

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
            # TODO: Use constant-str keys.
            self.assertTrue(resp_data == {
                "lat": lat_lng.lat,
                "lng": lat_lng.lng,
            })
