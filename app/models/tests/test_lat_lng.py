"""
Tests for the LatLng model.
"""

# External imports
import unittest

# Internal imports
from app.models.lat_lng import LatLng


class TestLatLng(unittest.TestCase):

    def test_create(self):
        lat_lng = LatLng(0.1, 1.0)
        self.assertTrue(lat_lng, "Instance should exist and be truthy")
        self.assertTrue(isinstance(lat_lng, LatLng),
                        "Instance should have type LatLng")

    def test_properties(self):
        lat = 1.1
        lng = 2.2
        lat_lng = LatLng(lat=lat, lng=lng)
        self.assertTrue(isinstance(lat_lng.lat, float),
                        "lat should be a float")
        self.assertTrue(isinstance(lat_lng.lng, float),
                        "lng should be a float")
        self.assertEqual(lat_lng.lat, lat,
                         "lat property should be the given lat value")
        self.assertEqual(lat_lng.lng, lng,
                         "lng property should be the given lng value")

    def test_equality(self):
        lat = 1.1
        lng = 2.2
        self.assertTrue(LatLng(lat=lat, lng=lng) == LatLng(lat=lat, lng=lng))

    def test_inequality(self):
        lat = 1.1
        lng = 2.2

        self.assertFalse(LatLng(lat=lat, lng=lng) == LatLng(
            lat=lng, lng=lat),
            "Swapped lat/lng values should lead to inequality")
        self.assertFalse(LatLng(lat=lat, lng=lng) ==
                         LatLng(lat=lat, lng=lng * 2),
                         "lng not equal, so instances should be not equal")
        self.assertFalse(LatLng(lat=lat, lng=lng) ==
                         LatLng(lat=lat * 2, lng=lng),
                         "lat not equal, so instances should be not equal")
        self.assertFalse(LatLng(lat=lat, lng=lng) ==
                         LatLng(lat=lat * 2, lng=lng * 2),
                         "lat and lng not equal, so instances should be not equal")  # NOQA: E501
